#!/bin/bash

# ============================================================
# 🌌 ANTIGRAVITY CONFIG INSTALLER
# ============================================================
# Transforms any Google Gemini IDE into a supercharged AI agent
# 
# Usage: ./install.sh [options]
#   --full    Install ALL skills (100+)
#   --minimal Install only core skills (12)
#   --help    Show this help message
# ============================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GEMINI_DIR="$HOME/.gemini"
PLAYGROUND_DIR="$HOME/playground"
AGENT_DIR="$PLAYGROUND_DIR/.agent"
CONFIG_REPO="$PLAYGROUND_DIR/repos/LuisSambrano/antigravity-config"

# Default mode
INSTALL_MODE="minimal"

# Parse arguments
for arg in "$@"; do
    case $arg in
        --full)
            INSTALL_MODE="full"
            shift
            ;;
        --minimal)
            INSTALL_MODE="minimal"
            shift
            ;;
        --help)
            echo "Usage: ./install.sh [options]"
            echo "  --full    Install ALL skills (100+)"
            echo "  --minimal Install only core skills (12, default)"
            echo "  --help    Show this help message"
            exit 0
            ;;
    esac
done

echo ""
echo -e "${PURPLE}╔═══════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║         🌌 ANTIGRAVITY CONFIG INSTALLER                  ║${NC}"
echo -e "${PURPLE}╚═══════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${CYAN}Mode: ${YELLOW}$INSTALL_MODE${NC}"
echo ""

# Step 1: Create directories
echo -e "${BLUE}[1/6]${NC} Creating directories..."
mkdir -p "$GEMINI_DIR"
mkdir -p "$AGENT_DIR/skills"
mkdir -p "$AGENT_DIR/workflows"
mkdir -p "$CONFIG_REPO"
echo -e "${GREEN}✓${NC} Directories created"

# Step 2: Copy GEMINI.md
echo -e "${BLUE}[2/6]${NC} Installing GEMINI.md..."
if [ -f "$GEMINI_DIR/GEMINI.md" ]; then
    echo -e "${YELLOW}  Backing up existing GEMINI.md...${NC}"
    cp "$GEMINI_DIR/GEMINI.md" "$GEMINI_DIR/GEMINI.md.backup.$(date +%Y%m%d_%H%M%S)"
fi
cp "$SCRIPT_DIR/GEMINI.md" "$GEMINI_DIR/GEMINI.md"
echo -e "${GREEN}✓${NC} GEMINI.md installed"

# Step 3: Copy Rules
echo -e "${BLUE}[3/6]${NC} Installing master rules..."
cp -r "$SCRIPT_DIR/rules" "$CONFIG_REPO/"
echo -e "${GREEN}✓${NC} Rules installed (5 files)"

# Step 4: Copy Workflows
echo -e "${BLUE}[4/6]${NC} Installing workflows..."
cp "$SCRIPT_DIR/workflows/"*.md "$AGENT_DIR/workflows/" 2>/dev/null || true
echo -e "${GREEN}✓${NC} Workflows installed (3 commands)"

# Step 5: Install Skills
echo -e "${BLUE}[5/6]${NC} Installing skills..."

CORE_SKILLS=(
    "web-development/nextjs-development"
    "web-development/frontend-design"
    "coding-standards/typescript-patterns"
    "ai-agents/prompt-engineering"
    "security/api-security-best-practices"
    "automation-tools/playwright-skill"
    "content-writing/technical-writing"
    "meta-skills/skill-creator"
)

if [ "$INSTALL_MODE" = "full" ]; then
    echo -e "${YELLOW}  Installing ALL skills (this may take a moment)...${NC}"
    # Create symlinks for all skill categories
    for category in "$SCRIPT_DIR/skills"/*/; do
        category_name=$(basename "$category")
        for skill in "$category"*/; do
            if [ -d "$skill" ]; then
                skill_name=$(basename "$skill")
                ln -sf "$skill" "$AGENT_DIR/skills/$skill_name" 2>/dev/null || true
            fi
        done
    done
    SKILL_COUNT=$(find "$AGENT_DIR/skills" -maxdepth 1 -type l | wc -l | tr -d ' ')
    echo -e "${GREEN}✓${NC} $SKILL_COUNT skills linked"
else
    echo -e "${YELLOW}  Installing core skills (12)...${NC}"
    for skill_path in "${CORE_SKILLS[@]}"; do
        skill_name=$(basename "$skill_path")
        full_path="$SCRIPT_DIR/skills/$skill_path"
        if [ -d "$full_path" ]; then
            ln -sf "$full_path" "$AGENT_DIR/skills/$skill_name"
            echo -e "    ${GREEN}✓${NC} $skill_name"
        fi
    done
fi

# Step 6: Verify installation
echo -e "${BLUE}[6/6]${NC} Verifying installation..."
ERRORS=0

if [ ! -f "$GEMINI_DIR/GEMINI.md" ]; then
    echo -e "${RED}✗${NC} GEMINI.md not found"
    ERRORS=$((ERRORS + 1))
fi

if [ ! -d "$CONFIG_REPO/rules" ]; then
    echo -e "${RED}✗${NC} Rules not found"
    ERRORS=$((ERRORS + 1))
fi

if [ ! -d "$AGENT_DIR/workflows" ]; then
    echo -e "${RED}✗${NC} Workflows not found"
    ERRORS=$((ERRORS + 1))
fi

if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✓${NC} All components verified"
else
    echo -e "${RED}✗${NC} $ERRORS errors found"
    exit 1
fi

# Summary
echo ""
echo -e "${PURPLE}╔═══════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║         🎉 INSTALLATION COMPLETE                          ║${NC}"
echo -e "${PURPLE}╚═══════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "Installed components:"
echo -e "  ${GREEN}✓${NC} GEMINI.md     → $GEMINI_DIR/GEMINI.md"
echo -e "  ${GREEN}✓${NC} Rules (5)     → $CONFIG_REPO/rules/"
echo -e "  ${GREEN}✓${NC} Workflows (3) → $AGENT_DIR/workflows/"
echo -e "  ${GREEN}✓${NC} Skills        → $AGENT_DIR/skills/"
echo ""
echo -e "${YELLOW}Next Steps:${NC}"
echo -e "  1. Restart your IDE"
echo -e "  2. Try: /status"
echo ""
echo -e "${CYAN}Your AI agent is now supercharged! 🚀${NC}"
echo ""
