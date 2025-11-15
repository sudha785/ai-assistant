import os
from typing import List, Dict, Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

# Get your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    # This will show clearly in the backend if key is missing
    raise RuntimeError("OPENAI_API_KEY is not set in .env")

client = OpenAI(api_key=api_key)

app = FastAPI()

# 🔹 CORS SETTINGS – allow your frontend on 5500
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    messages: List[Dict[str, Any]]

@app.get("/")
async def root():
    return {"status": "ok", "message": "AI backend running"}

@app.post("/chat")
async def chat_endpoint(body: ChatRequest):
    """
    Expects:
    {
      "messages": [
        {"role": "user", "content": "Hello"}
      ]
    }
    """
    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=body.messages,
    )

    reply_message = completion.choices[0].message

    return {
        "reply": {
            "role": reply_message.role,
            "content": reply_message.content,
        }
    }
