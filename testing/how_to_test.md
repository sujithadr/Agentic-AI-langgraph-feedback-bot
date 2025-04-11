# 🧪 Testing Guide for LangGraph Feedback Classifier

This document helps validate the functionality of the OpenAI LLM-powered LangGraph project.

---

## ✅ How to Run

From the project root, activate your environment and run:

```bash
python project/main.py
```

Make sure `.env` is configured with:

```env
OPENAI_API_KEY=your-api-key
MODEL_NAME=gpt-4
```

---

## 🧪 Test Cases

### 1. Question Input

```json
{
  "customer_remark": "Why did you increase the price?"
}
```

**Expected:**
- Route: `question`
- Tag: `Pricing`
- Final Message: includes `Pricing Department`

---

### 2. Compliment Input

```json
{
  "customer_remark": "Nice work on the new packaging!"
}
```

**Expected:**
- Route: `compliment`
- Tag: `Packaging`
- Final Message: includes `Packaging Department`

---

### 3. General Feedback

```json
{
  "customer_remark": "Okay-ish experience overall"
}
```

**Expected:**
- Route: Either (based on LLM)
- Tag: `General`

---

## 🔍 Debugging Tips

### Print intermediate state
Add in any handler:
```python
print("DEBUG STATE:", state)
```

---

### Use Graph Stream
To visualize each graph transition:
```python
for step in graph.stream(input_payload):
    print(step)
```

---

## 🛑 Common Issues

| Issue | Fix |
|-------|-----|
| API Key Error | Check `.env` values |
| No Response | Add `print()` in nodes |
| Unexpected Output | Use `graph.stream()` |

---

Happy testing! 🚀
