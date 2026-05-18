# 🤖 Anthropic Streaming AI Assistant

A production-style Python project demonstrating:

* Anthropic tool calling
* Built-in web search
* Real-time streaming responses
* HTML chatbot frontend
* FastAPI backend integration
* Dockerized deployment

using the official Anthropic SDK.

This project shows how Claude can:

* Decide when to call tools
* Execute Python functions
* Fetch live weather data
* Search the web for real-time information
* Stream responses in real-time
* Continue multi-turn conversations
* Return tool results back to the model

---

# 🚀 Features

* Anthropic tool calling
* Built-in web search via `web_search_20250305`
* Real-time streaming responses
* SSE (Server-Sent Events) streaming
* HTML/CSS chatbot frontend
* FastAPI backend
* Multi-turn chat memory
* Live weather API integration
* Open-Meteo weather API
* Markdown rendering support
* Modular architecture
* Docker support
* Docker Compose support
* Environment variable management with dotenv

---

# 📦 Installation

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

---

# ▶️ Run Locally

```bash
uvicorn app:app --reload
```

Open in browser:

```bash
http://127.0.0.1:8000
```

---

# 🐳 Run With Docker

## Build Containers

```bash
docker compose build
```

## Start Application

```bash
docker compose up
```

Open in browser:

```bash
http://localhost:8000
```

---

# 💬 Example Conversation

```bash
You: What is the weather in Delhi?

Claude: The current weather in Delhi is 36°C.

You: Latest AI news

🌐 Claude is searching the web...

Claude: Here's a roundup of the latest AI news...
```

---

# 📁 Project Structure

```bash
anthropic-chatbot/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
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
├── chatbot/
│   └── chatbot.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# 🛠️ Tech Stack

* Python
* FastAPI
* Anthropic SDK
* Claude Sonnet 4.6
* Open-Meteo API
* HTML/CSS/JavaScript
* SSE Streaming
* Docker
* Docker Compose
* python-dotenv

---

# ✅ Current Capabilities

* Streaming AI responses
* Built-in web search
* Weather tool calling
* Real-time frontend updates
* Multi-turn conversations
* Modular backend architecture
* HTML chatbot UI
* Markdown response rendering
* Dockerized deployment

---