# 🤖 Anthropic Conversational Weather Assistant

A simple Python project demonstrating **Anthropic tool/function calling** using the official Anthropic SDK and `python-dotenv`.

This project shows how Claude can:

- Decide when to call a tool
- Execute Python functions
- Fetch live weather data from an external API
- Continue multi-turn conversations
- Answer follow-up weather questions
- Return tool results back to the model

---

## 🚀 Features

- Anthropic tool calling
- Conversational AI assistant
- Multi-turn chat memory
- Live weather API integration
- Open-Meteo weather API
- Local Python function execution
- Environment variable management with dotenv
- Beginner-friendly implementation

---

## 📦 Installation

```bash
pip install anthropic python-dotenv
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 💬 Example Conversation

```bash
You: What is the weather in Delhi?

Claude: The current weather in Delhi is 36°C.

You: Is it good for walking outside?

Claude: 36°C is quite hot for long walks outside...
```

---

## 📁 Project Structure

```bash
.
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

- Python
- Anthropic SDK
- Claude Sonnet 4.6
- Open-Meteo API
- python-dotenv