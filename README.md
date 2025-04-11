# LangGraph Feedback Classifier (OpenAI LLM Powered)

A LangGraph project that classifies customer remarks as questions or compliments using OpenAI GPT, tags them by context, and returns beautified responses.

**Author:** Sujith Somanunnithan  
**GitHub:** [github.com/sujithsom/langgraph-feedback-bot](https://github.com/sujithadr/Agentic-AI-langgraph-feedback-bot)

---

## 📦 Features

- ✅ Uses OpenAI GPT to classify inputs: compliment or question
- 🧠 Conditional routing in LangGraph based on LLM results
- 🏷 Context-aware tagging: Packaging, Pricing, or General
- ✨ Beautifies responses with structured handoff messages
- ♻️ Modular and scalable project structure

---

## 🛠 Project Structure

```
langgraph-feedback-bot/
├── project/
│   ├── main.py                # Entry point to invoke the graph
│   ├── graph_builder.py       # Builds the LangGraph graph
│   ├── handlers.py            # Node handlers: extract, tag, beautify
│   ├── operators.py           # Custom merge functions
│   ├── state.py               # State schema
│   └── __init__.py
├── testing/
│   └── how_to_test.md         # Testing instructions
├── .env                       # LLM config
├── requirements.txt           # Required packages
├── README.md                  # You're reading it
├── template.py                # Script to scaffold folders
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sujithsom/langgraph-feedback-bot.git
cd langgraph-feedback-bot
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure OpenAI

Create a `.env` file with:
```env
OPENAI_API_KEY=your-openai-api-key
MODEL_NAME=gpt-4
```

---

## 💡 Example Usage

Run the application:

```bash
python project/main.py
```

Sample output:

```json
{
  "text": "Why is the price so high?",
  "tag": "Pricing",
  "answer": {
    "temp_answer": "Wow nice question.",
    "final_beautified_answer": [
      "Wow nice question. I will pass it to the Pricing Department"
    ]
  },
  "payload": [...]
}
```

---

## 🧪 Testing Guide

You can stream steps in real-time using:

```python
for step in graph.stream(payload):
    print(step)
```

See `testing/how_to_test.md` for test cases and expected outputs.

---

## 🔍 How It Works

### Core Flow

1. Extract comment → `text`
2. Classify as question or compliment → using GPT
3. Route to respective node
4. Tag based on content → Packaging, Pricing, General
5. Beautify final message

---

## 📚 Tech Stack

- LangGraph
- LangChain
- OpenAI GPT (via ChatOpenAI)
- Python 3.10+
- dotenv

---

## 📄 License

MIT © Sujith Somanunnithan
