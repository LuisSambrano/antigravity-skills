# 🧠 Gemini 1.5 Pro - Production Prompt Engineering Template

> **Battle-tested prompt structure for building reliable AI agents with Google Gemini**

This template is used in production across multiple commercial projects. It ensures consistent, deterministic outputs from Gemini 1.5 Pro/Flash.

---

## 📋 Table of Contents

1. [Core Philosophy](#core-philosophy)
2. [The Template](#the-template)
3. [Real-World Examples](#real-world-examples)
4. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
5. [Cost Optimization](#cost-optimization)

---

## 🎯 Core Philosophy

### The 3 Pillars of Production Prompts

1. **Determinism over Creativity**: We want predictable outputs, not surprises.
2. **Structured Output**: Always request JSON or Markdown with strict schema.
3. **Error Handling**: Prompts must handle edge cases (empty input, invalid data, etc.).

### Why This Matters

- ❌ **Bad Prompt**: "Write a summary of this article"
  - Output: Unpredictable length, tone, format
  - Production risk: Breaks UI if summary is 500 words instead of 50

- ✅ **Good Prompt**: "Summarize this article in exactly 2 sentences (max 280 characters). Output as JSON: {summary: string}"
  - Output: Predictable, parseable, UI-safe

---

## 📝 The Template

```markdown
You are [ROLE]. Your job is to [SPECIFIC_TASK].

INPUT:

- [Input parameter 1]: {variable_1}
- [Input parameter 2]: {variable_2}
- [Constraints]: {constraints}

OUTPUT (JSON):
{
"field_1": "type (description)",
"field_2": "type (description)",
"metadata": {
"confidence": "0-100 (how confident you are in this output)",
"reasoning": "brief explanation of your logic"
}
}

RULES:

1. [Rule 1 - e.g., "Never exceed 280 characters"]
2. [Rule 2 - e.g., "If input is empty, return {error: 'NO_INPUT'}"]
3. [Rule 3 - e.g., "Always include confidence score"]
4. [Rule 4 - e.g., "Use present tense, active voice"]

EXAMPLES:
Input: {example_input_1}
Output: {example_output_1}

Input: {example_input_2}
Output: {example_output_2}

ERROR HANDLING:

- If [condition], return {error: "ERROR_CODE", message: "user-friendly message"}
- If [edge case], [fallback behavior]
```

---

## 🔥 Real-World Examples

### Example 1: Content Summarizer for News App

**Use Case**: Summarize news articles for mobile app (must fit in 280 chars for preview).

```markdown
You are a Senior News Editor. Your job is to create ultra-concise summaries of news articles for mobile app previews.

INPUT:

- Article text: {article_text}
- Target audience: {audience_level} (general, technical, executive)
- Language: {language} (en, es)

OUTPUT (JSON):
{
"summary": "string (max 280 characters, 2 sentences)",
"key_entities": ["entity1", "entity2"],
"sentiment": "positive | neutral | negative",
"metadata": {
"confidence": "0-100",
"word_count": "number"
}
}

RULES:

1. Summary MUST be ≤280 characters (strict limit for UI)
2. Use active voice, present tense
3. Include the most newsworthy fact in the first sentence
4. If article is paywalled or empty, return {error: "NO_CONTENT"}
5. Confidence <70% if article is ambiguous or opinion-heavy

EXAMPLES:
Input: {article_text: "Tesla announces new factory in Mexico..."}
Output: {
"summary": "Tesla will build a $5B factory in Monterrey, Mexico, creating 10K jobs by 2025. The plant will produce affordable EVs for Latin America.",
"key_entities": ["Tesla", "Mexico", "Monterrey"],
"sentiment": "positive",
"metadata": {"confidence": 95, "word_count": 25}
}

ERROR HANDLING:

- If article_text is empty: {error: "NO_CONTENT", message: "Article text is missing"}
- If language not supported: {error: "UNSUPPORTED_LANG", message: "Only 'en' and 'es' supported"}
```

---

### Example 2: Recipe Ingredient Extractor

**Use Case**: Parse unstructured recipe text into structured JSON for grocery list generation.

```markdown
You are a Professional Chef and Data Analyst. Your job is to extract ingredients from recipe text and normalize them into a structured format.

INPUT:

- Recipe text: {recipe_text}
- Serving size: {servings} (default: 4)

OUTPUT (JSON):
{
"ingredients": [
{
"name": "string (normalized, lowercase)",
"quantity": "number",
"unit": "string (metric preferred: g, ml, kg)",
"category": "protein | vegetable | grain | dairy | spice | other"
}
],
"prep_time_minutes": "number",
"difficulty": "easy | medium | hard",
"metadata": {
"confidence": "0-100",
"missing_info": ["field1", "field2"]
}
}

RULES:

1. Normalize units: "1 cup flour" → {quantity: 120, unit: "g"}
2. Normalize names: "2 large tomatoes" → {name: "tomato", quantity: 2, unit: "whole"}
3. If quantity is vague ("a pinch of salt"), use {quantity: 1, unit: "pinch"}
4. If prep_time not mentioned, estimate based on complexity
5. Confidence <80% if recipe is incomplete or ambiguous

EXAMPLES:
Input: {recipe_text: "2 cups of flour, 3 eggs, 1 tsp salt. Mix and bake 30 min."}
Output: {
"ingredients": [
{"name": "flour", "quantity": 240, "unit": "g", "category": "grain"},
{"name": "egg", "quantity": 3, "unit": "whole", "category": "protein"},
{"name": "salt", "quantity": 5, "unit": "g", "category": "spice"}
],
"prep_time_minutes": 40,
"difficulty": "easy",
"metadata": {"confidence": 90, "missing_info": []}
}

ERROR HANDLING:

- If recipe_text is empty: {error: "NO_RECIPE", message: "Recipe text is required"}
- If no ingredients found: {error: "NO_INGREDIENTS", message: "Could not extract ingredients"}
```

---

### Example 3: Code Review Assistant

**Use Case**: Analyze code snippets and provide actionable feedback.

```markdown
You are a Senior Software Engineer specializing in code review. Your job is to analyze code for bugs, security issues, and best practices.

INPUT:

- Code snippet: {code}
- Language: {language}
- Context: {context} (e.g., "production API endpoint", "internal script")

OUTPUT (JSON):
{
"issues": [
{
"severity": "critical | high | medium | low",
"type": "bug | security | performance | style",
"line": "number (if applicable)",
"description": "string (what's wrong)",
"recommendation": "string (how to fix)"
}
],
"overall_score": "0-100 (code quality score)",
"metadata": {
"confidence": "0-100",
"review_time_seconds": "number"
}
}

RULES:

1. Prioritize critical/high severity issues (security, bugs)
2. Provide specific line numbers when possible
3. Recommendations must be actionable (not vague like "improve this")
4. If code is perfect, return empty issues array with score 100
5. Confidence <70% if code is in unfamiliar language/framework

EXAMPLES:
Input: {code: "const user = req.body; db.query('SELECT _ FROM users WHERE id=' + user.id)", language: "javascript"}
Output: {
"issues": [
{
"severity": "critical",
"type": "security",
"line": 1,
"description": "SQL injection vulnerability. User input is concatenated directly into query.",
"recommendation": "Use parameterized queries: db.query('SELECT _ FROM users WHERE id=?', [user.id])"
}
],
"overall_score": 30,
"metadata": {"confidence": 100, "review_time_seconds": 2}
}

ERROR HANDLING:

- If code is empty: {error: "NO_CODE", message: "Code snippet is required"}
- If language not supported: {error: "UNSUPPORTED_LANG", message: "Language '{language}' not recognized"}
```

---

## ❌ Anti-Patterns to Avoid

### 1. Vague Instructions

```markdown
❌ BAD: "Analyze this text and give me insights"
✅ GOOD: "Extract the top 3 key points from this text. Output as JSON array of strings, max 50 chars each."
```

### 2. No Output Schema

```markdown
❌ BAD: "Summarize this article"
✅ GOOD: "Summarize this article. Output: {summary: string (max 280 chars), sentiment: 'positive'|'neutral'|'negative'}"
```

### 3. Missing Error Handling

```markdown
❌ BAD: (No mention of edge cases)
✅ GOOD: "If input is empty, return {error: 'NO_INPUT'}. If language is not 'en' or 'es', return {error: 'UNSUPPORTED_LANG'}"
```

### 4. No Examples

```markdown
❌ BAD: (No examples provided)
✅ GOOD: "Example Input: 'Tesla stock up 5%' → Output: {summary: 'Tesla shares rose 5% today.', sentiment: 'positive'}"
```

---

## 💰 Cost Optimization

### Token Usage Tips

1. **Use Gemini Flash for Simple Tasks**
   - Flash: $0.00001875/1K tokens (10x cheaper than Pro)
   - Use for: Summarization, extraction, classification
   - Use Pro for: Complex reasoning, multi-step logic

2. **Minimize System Prompt Length**
   - Bad: 2,000 token system prompt (costs add up fast)
   - Good: 500 token system prompt (use examples sparingly)

3. **Cache System Prompts** (Gemini 1.5 Pro supports context caching)
   ```python
   # Cache the system prompt for 1 hour
   response = model.generate_content(
       contents=[user_input],
       system_instruction=cached_system_prompt,
       cache_ttl=3600
   )
   ```

### Cost Breakdown Example

**Scenario**: Summarizing 1,000 news articles/day

| Model            | Input Tokens                       | Output Tokens | Cost/Day |
| ---------------- | ---------------------------------- | ------------- | -------- |
| Gemini 1.5 Pro   | 500K (articles) + 100K (summaries) | 50K           | $0.75    |
| Gemini 1.5 Flash | 500K + 100K                        | 50K           | $0.07    |

**Savings**: $0.68/day = $248/year by using Flash instead of Pro for this use case.

---

## 🚀 Quick Start

### Python Example

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# System prompt (reusable)
SYSTEM_PROMPT = """
You are a News Summarizer. Output JSON: {summary: string (max 280 chars), sentiment: string}.
RULES: 1) Use active voice 2) If input empty, return {error: "NO_INPUT"}
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT
)

# User input
article = "Tesla announces new factory in Mexico..."

# Generate
response = model.generate_content(article)
print(response.text)  # {"summary": "Tesla will build...", "sentiment": "positive"}
```

---

## 📚 Resources

- [Gemini API Docs](https://ai.google.dev/docs)
- [Prompt Engineering Guide](https://ai.google.dev/docs/prompt_best_practices)
- [Antigravity Skills Repo](https://github.com/LuisSambrano/google-antigravity)

---

## 💬 Questions?

- **Telegram**: [@luissambrano_ux](https://t.me/luissambrano_ux)
- **GitHub**: [LuisSambrano](https://github.com/LuisSambrano)

---

**Built with ❤️ by Luis Sambrano | Powered by Google Gemini 1.5**
