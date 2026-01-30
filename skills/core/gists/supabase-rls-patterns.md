# 🛡️ Supabase RLS Policies - Real-World Patterns

> **Production-tested Row Level Security patterns for common application architectures**

This guide covers battle-tested RLS (Row Level Security) policies for Supabase/PostgreSQL. These patterns are used in production SaaS apps, marketplaces, and social platforms.

---

## 📋 Table of Contents

1. [RLS Fundamentals](#rls-fundamentals)
2. [Pattern 1: Multi-Tenant SaaS](#pattern-1-multi-tenant-saas)
3. [Pattern 2: Social Platform](#pattern-2-social-platform)
4. [Pattern 3: Marketplace (Buyers + Sellers)](#pattern-3-marketplace-buyers--sellers)
5. [Pattern 4: Team Collaboration](#pattern-4-team-collaboration)
6. [Common Pitfalls](#common-pitfalls)
7. [Testing RLS](#testing-rls)

---

## 🎯 RLS Fundamentals

### What is RLS?

Row Level Security (RLS) is PostgreSQL's built-in feature that **filters rows based on the current user**. Think of it as "WHERE user_id = current_user" automatically applied to every query.

### Why Use RLS?

- ✅ **Security**: Users can't access other users' data, even if they modify the SQL query
- ✅ **Simplicity**: No need to add `WHERE user_id = ?` to every query in your app code
- ✅ **Audit-friendly**: Database enforces access control, not application logic

### The Golden Rule

> **"Enable RLS on EVERY table that contains user data. No exceptions."**

---

## 🏢 Pattern 1: Multi-Tenant SaaS

**Use Case**: B2B SaaS where each company (organization) has multiple users. Users should only see data from their own organization.

### Schema

```sql
-- Organizations (companies)
CREATE TABLE organizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Users belong to organizations
CREATE TABLE users (
    id UUID PRIMARY KEY REFERENCES auth.users,
    organization_id UUID REFERENCES organizations NOT NULL,
    role TEXT NOT NULL DEFAULT 'member', -- 'admin', 'member', 'viewer'
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Projects (scoped to organization)
CREATE TABLE projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES organizations NOT NULL,
    name TEXT NOT NULL,
    created_by UUID REFERENCES users,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### RLS Policies

```sql
-- Enable RLS
ALTER TABLE organizations ENABLE ROW LEVEL SECURITY;
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE projects ENABLE ROW LEVEL SECURITY;

-- Organizations: Users can only see their own org
CREATE POLICY "Users can view their own organization"
    ON organizations FOR SELECT
    USING (
        id IN (
            SELECT organization_id
            FROM users
            WHERE id = auth.uid()
        )
    );

-- Users: Can see other users in same org
CREATE POLICY "Users can view users in their organization"
    ON users FOR SELECT
    USING (
        organization_id IN (
            SELECT organization_id
            FROM users
            WHERE id = auth.uid()
        )
    );

-- Users: Only admins can insert new users
CREATE POLICY "Admins can invite users"
    ON users FOR INSERT
    WITH CHECK (
        EXISTS (
            SELECT 1 FROM users
            WHERE id = auth.uid()
            AND organization_id = users.organization_id
            AND role = 'admin'
        )
    );

-- Projects: Users can view projects in their org
CREATE POLICY "Users can view projects in their organization"
    ON projects FOR SELECT
    USING (
        organization_id IN (
            SELECT organization_id
            FROM users
            WHERE id = auth.uid()
        )
    );

-- Projects: Any member can create projects
CREATE POLICY "Members can create projects"
    ON projects FOR INSERT
    WITH CHECK (
        organization_id IN (
            SELECT organization_id
            FROM users
            WHERE id = auth.uid()
        )
    );

-- Projects: Only creator or admin can delete
CREATE POLICY "Creator or admin can delete projects"
    ON projects FOR DELETE
    USING (
        created_by = auth.uid()
        OR EXISTS (
            SELECT 1 FROM users
            WHERE id = auth.uid()
            AND organization_id = projects.organization_id
            AND role = 'admin'
        )
    );
```

---

## 👥 Pattern 2: Social Platform

**Use Case**: Social network where users have public profiles, private posts, and followers.

### Schema

```sql
-- User profiles (public info)
CREATE TABLE profiles (
    id UUID PRIMARY KEY REFERENCES auth.users,
    username TEXT UNIQUE NOT NULL,
    bio TEXT,
    avatar_url TEXT,
    is_private BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Posts
CREATE TABLE posts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES profiles NOT NULL,
    content TEXT NOT NULL,
    visibility TEXT DEFAULT 'public', -- 'public', 'followers', 'private'
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Followers
CREATE TABLE followers (
    follower_id UUID REFERENCES profiles NOT NULL,
    following_id UUID REFERENCES profiles NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (follower_id, following_id)
);
```

### RLS Policies

```sql
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE posts ENABLE ROW LEVEL SECURITY;
ALTER TABLE followers ENABLE ROW LEVEL SECURITY;

-- Profiles: Everyone can view public profiles
CREATE POLICY "Anyone can view public profiles"
    ON profiles FOR SELECT
    USING (
        NOT is_private
        OR id = auth.uid()
        OR EXISTS (
            SELECT 1 FROM followers
            WHERE following_id = profiles.id
            AND follower_id = auth.uid()
        )
    );

-- Profiles: Users can update their own profile
CREATE POLICY "Users can update own profile"
    ON profiles FOR UPDATE
    USING (id = auth.uid())
    WITH CHECK (id = auth.uid());

-- Posts: View based on visibility
CREATE POLICY "Users can view posts based on visibility"
    ON posts FOR SELECT
    USING (
        visibility = 'public'
        OR user_id = auth.uid()
        OR (
            visibility = 'followers'
            AND EXISTS (
                SELECT 1 FROM followers
                WHERE following_id = posts.user_id
                AND follower_id = auth.uid()
            )
        )
    );

-- Posts: Users can create their own posts
CREATE POLICY "Users can create own posts"
    ON posts FOR INSERT
    WITH CHECK (user_id = auth.uid());

-- Posts: Users can delete their own posts
CREATE POLICY "Users can delete own posts"
    ON posts FOR DELETE
    USING (user_id = auth.uid());

-- Followers: Users can follow anyone
CREATE POLICY "Users can follow others"
    ON followers FOR INSERT
    WITH CHECK (follower_id = auth.uid());

-- Followers: Users can unfollow
CREATE POLICY "Users can unfollow"
    ON followers FOR DELETE
    USING (follower_id = auth.uid());

-- Followers: Users can see who follows whom
CREATE POLICY "Anyone can view followers"
    ON followers FOR SELECT
    USING (TRUE);
```

---

## 🛒 Pattern 3: Marketplace (Buyers + Sellers)

**Use Case**: Two-sided marketplace (e.g., Airbnb, Etsy) where sellers list products and buyers purchase them.

### Schema

```sql
-- Sellers
CREATE TABLE sellers (
    id UUID PRIMARY KEY REFERENCES auth.users,
    shop_name TEXT NOT NULL,
    stripe_account_id TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Products
CREATE TABLE products (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    seller_id UUID REFERENCES sellers NOT NULL,
    name TEXT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    is_published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Orders
CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    buyer_id UUID REFERENCES auth.users NOT NULL,
    seller_id UUID REFERENCES sellers NOT NULL,
    product_id UUID REFERENCES products NOT NULL,
    status TEXT DEFAULT 'pending', -- 'pending', 'paid', 'shipped', 'completed'
    total_amount DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### RLS Policies

```sql
ALTER TABLE sellers ENABLE ROW LEVEL SECURITY;
ALTER TABLE products ENABLE ROW LEVEL SECURITY;
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

-- Sellers: Anyone can view seller profiles
CREATE POLICY "Anyone can view sellers"
    ON sellers FOR SELECT
    USING (TRUE);

-- Sellers: Only the seller can update their profile
CREATE POLICY "Sellers can update own profile"
    ON sellers FOR UPDATE
    USING (id = auth.uid());

-- Products: Anyone can view published products
CREATE POLICY "Anyone can view published products"
    ON products FOR SELECT
    USING (is_published = TRUE OR seller_id = auth.uid());

-- Products: Sellers can create products
CREATE POLICY "Sellers can create products"
    ON products FOR INSERT
    WITH CHECK (seller_id = auth.uid());

-- Products: Sellers can update their own products
CREATE POLICY "Sellers can update own products"
    ON products FOR UPDATE
    USING (seller_id = auth.uid());

-- Orders: Buyers can view their own orders
CREATE POLICY "Buyers can view own orders"
    ON orders FOR SELECT
    USING (buyer_id = auth.uid() OR seller_id = auth.uid());

-- Orders: Buyers can create orders
CREATE POLICY "Buyers can create orders"
    ON orders FOR INSERT
    WITH CHECK (buyer_id = auth.uid());

-- Orders: Sellers can update order status
CREATE POLICY "Sellers can update order status"
    ON orders FOR UPDATE
    USING (seller_id = auth.uid())
    WITH CHECK (seller_id = auth.uid());
```

---

## 👨‍💼 Pattern 4: Team Collaboration

**Use Case**: Project management tool where teams have workspaces, projects, and tasks with granular permissions.

### Schema

```sql
-- Workspaces
CREATE TABLE workspaces (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Workspace members
CREATE TABLE workspace_members (
    workspace_id UUID REFERENCES workspaces NOT NULL,
    user_id UUID REFERENCES auth.users NOT NULL,
    role TEXT NOT NULL, -- 'owner', 'admin', 'member', 'guest'
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (workspace_id, user_id)
);

-- Tasks
CREATE TABLE tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    workspace_id UUID REFERENCES workspaces NOT NULL,
    title TEXT NOT NULL,
    assigned_to UUID REFERENCES auth.users,
    created_by UUID REFERENCES auth.users NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### RLS Policies

```sql
ALTER TABLE workspaces ENABLE ROW LEVEL SECURITY;
ALTER TABLE workspace_members ENABLE ROW LEVEL SECURITY;
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;

-- Workspaces: Members can view their workspaces
CREATE POLICY "Members can view their workspaces"
    ON workspaces FOR SELECT
    USING (
        id IN (
            SELECT workspace_id
            FROM workspace_members
            WHERE user_id = auth.uid()
        )
    );

-- Workspace members: Members can view other members
CREATE POLICY "Members can view workspace members"
    ON workspace_members FOR SELECT
    USING (
        workspace_id IN (
            SELECT workspace_id
            FROM workspace_members
            WHERE user_id = auth.uid()
        )
    );

-- Workspace members: Owners/admins can add members
CREATE POLICY "Admins can add members"
    ON workspace_members FOR INSERT
    WITH CHECK (
        EXISTS (
            SELECT 1 FROM workspace_members
            WHERE workspace_id = workspace_members.workspace_id
            AND user_id = auth.uid()
            AND role IN ('owner', 'admin')
        )
    );

-- Tasks: Members can view tasks in their workspace
CREATE POLICY "Members can view workspace tasks"
    ON tasks FOR SELECT
    USING (
        workspace_id IN (
            SELECT workspace_id
            FROM workspace_members
            WHERE user_id = auth.uid()
        )
    );

-- Tasks: Members can create tasks
CREATE POLICY "Members can create tasks"
    ON tasks FOR INSERT
    WITH CHECK (
        workspace_id IN (
            SELECT workspace_id
            FROM workspace_members
            WHERE user_id = auth.uid()
        )
        AND created_by = auth.uid()
    );

-- Tasks: Assigned user or creator can update
CREATE POLICY "Assigned user can update task"
    ON tasks FOR UPDATE
    USING (
        assigned_to = auth.uid()
        OR created_by = auth.uid()
    );
```

---

## ❌ Common Pitfalls

### 1. Forgetting to Enable RLS

```sql
-- ❌ BAD: Table created but RLS not enabled
CREATE TABLE sensitive_data (id UUID, user_id UUID, secret TEXT);
-- Anyone can query: SELECT * FROM sensitive_data;

-- ✅ GOOD: Always enable RLS
ALTER TABLE sensitive_data ENABLE ROW LEVEL SECURITY;
```

### 2. Overly Permissive Policies

```sql
-- ❌ BAD: Allows anyone to see everything
CREATE POLICY "bad_policy" ON posts FOR SELECT USING (TRUE);

-- ✅ GOOD: Restrict to owner or public posts
CREATE POLICY "good_policy" ON posts FOR SELECT
USING (user_id = auth.uid() OR visibility = 'public');
```

### 3. Missing `WITH CHECK` on INSERT/UPDATE

```sql
-- ❌ BAD: User can insert data for other users
CREATE POLICY "bad_insert" ON posts FOR INSERT
USING (user_id = auth.uid());

-- ✅ GOOD: Enforce user_id on insert
CREATE POLICY "good_insert" ON posts FOR INSERT
WITH CHECK (user_id = auth.uid());
```

### 4. N+1 Queries in RLS Policies

```sql
-- ❌ BAD: Subquery runs for every row (slow)
CREATE POLICY "slow_policy" ON posts FOR SELECT
USING (
    user_id IN (SELECT user_id FROM followers WHERE follower_id = auth.uid())
);

-- ✅ BETTER: Use EXISTS (faster)
CREATE POLICY "fast_policy" ON posts FOR SELECT
USING (
    EXISTS (
        SELECT 1 FROM followers
        WHERE follower_id = auth.uid()
        AND following_id = posts.user_id
    )
);
```

---

## 🧪 Testing RLS

### Test as Different Users

```sql
-- Set the current user (simulates auth.uid())
SET LOCAL role TO authenticated;
SET LOCAL request.jwt.claims TO '{"sub": "user-uuid-here"}';

-- Test query
SELECT * FROM posts;

-- Reset
RESET role;
```

### Automated Testing (JavaScript)

```javascript
import { createClient } from "@supabase/supabase-js";

const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// Test as User A
const { data: userAPosts } = await supabase
  .from("posts")
  .select("*")
  .auth(USER_A_JWT);

console.assert(
  userAPosts.every((p) => p.user_id === USER_A_ID),
  "User A should only see their posts",
);

// Test as User B
const { data: userBPosts } = await supabase
  .from("posts")
  .select("*")
  .auth(USER_B_JWT);

console.assert(
  userBPosts.every((p) => p.user_id === USER_B_ID),
  "User B should only see their posts",
);
```

---

## 📚 Resources

- [Supabase RLS Docs](https://supabase.com/docs/guides/auth/row-level-security)
- [PostgreSQL RLS](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
- [Antigravity Skills Repo](https://github.com/LuisSambrano/google-antigravity)

---

## 💬 Questions?

- **Telegram**: [@luissambrano_ux](https://t.me/luissambrano_ux)
- **GitHub**: [LuisSambrano](https://github.com/LuisSambrano)

---

**Built with ❤️ by Luis Sambrano | Powered by Supabase + PostgreSQL**
