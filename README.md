# 🤖 Anthropic Function Calling Demo

A simple Python project demonstrating **Anthropic tool/function calling** using the official Anthropic SDK and `python-dotenv`.

This project shows how Claude can:

- Decide when to call a tool
- Execute Python functions
- Fetch live weather data from an external API
- Return tool results back to the model

---

## 🚀 Features

- Anthropic tool calling
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