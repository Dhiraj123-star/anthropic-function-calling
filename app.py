from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from chatbot.chatbot import AnthropicChatbot

app = FastAPI(title="Anthropic AI Assistant")
templates = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"),name="static")

# One chatbot instance per server process (single-user dev server).
# For multi-user production, store sessions in a dict keyed by session ID.
bot = AnthropicChatbot()


class ChatRequest(BaseModel):
    message: str


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/chat")
async def chat(payload: ChatRequest):
    """
    Returns a streaming SSE response.
    Each line is:  data: <json>\n\n
    """

    def event_generator():
        for chunk in bot.chat_stream(payload.message):
            yield f"data: {chunk}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",   # disable nginx buffering if behind a proxy
        },
    )


@app.post("/reset")
async def reset():
    """Clear conversation history."""
    bot.messages.clear()
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)