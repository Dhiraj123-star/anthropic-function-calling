# 🤖 Anthropic AI Assistant

A Python project demonstrating **Anthropic tool calling and built-in web search** using the official Anthropic SDK.

This project shows how Claude can:

- Decide when to call a tool
- Execute Python functions
- Fetch live weather data from an external API
- Search the web for real-time information
- Continue multi-turn conversations
- Return tool results back to the model

---

## 🚀 Features

- Anthropic tool calling
- Built-in web search via `web_search_20250305`
- Conversational AI assistant
- Multi-turn chat memory
- Live weather API integration
- Open-Meteo weather API
- Environment variable management with dotenv
- Clean modular architecture

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

You: Latest AI news
🌐 Claude is searching the web...
Claude: Here's a roundup of the latest AI news...
```

---

## 📁 Project Structure

```bash
anthropic-chatbot/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
├── config/
│   └── settings.py
│
├── services/
│   ├── anthropic_service.py
│   └── weather_service.py
│
├── tools/
│   └── tools.py
│
└── chatbot/
    └── chatbot.py
```

---

## 🛠️ Tech Stack

- Python
- Anthropic SDK
- Claude Sonnet 4.6
- Open-Meteo API
- python-dotenv