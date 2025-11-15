🤖 AI Assistant (ChatGPT-Style Web App)

A simple, fully working AI chatbot built with:

FastAPI (Python backend)

OpenAI API

HTML, CSS, JavaScript (frontend)

CORS-enabled communication

Local development server

This project lets you run your own ChatGPT-style assistant locally with a clean UI and working backend.

🚀 Features

AI-powered responses using OpenAI models

FastAPI backend for performance

Modern chat UI with auto-scroll

Conversation memory

Frontend ↔ Backend API communication

Secure API key using .env

Fully functional and ready to deploy

📂 Project Structure

AI-ASSISTANT/
backend/
main.py
.env
requirements.txt
frontend/
index.html

🔧 Installation & Setup

Clone the repository:

git clone https://github.com/YOUR-USERNAME/ai-assistant.git

cd ai-assistant

🛠 Backend Setup (FastAPI)

Enter backend folder:
cd backend

Install dependencies:
pip install -r requirements.txt

Create a .env file inside backend/:
OPENAI_API_KEY=your_api_key_here

Run the backend server:
python -m uvicorn main:app --reload --port 8000

Backend URL:
http://127.0.0.1:8000

Docs:
http://127.0.0.1:8000/docs

🎨 Frontend Setup

Start a local server:

Open another terminal:
cd frontend
python -m http.server 5500

Frontend URL:
http://127.0.0.1:5500/index.html

💬 Using the Chatbot

Make sure both servers are running:

Backend: http://127.0.0.1:8000

Frontend: http://127.0.0.1:5500

Open the frontend

Type a message

Enjoy AI responses

📦 Technologies Used

Python 3

FastAPI

OpenAI Python SDK

Pydantic

JavaScript (fetch API)

HTML / CSS

CORS Middleware

🔐 Important
Do NOT commit your .env file.
It is ignored using .gitignore.

📄 License
This project is free to use for learning, experimenting, and personal use.

⭐ Future Improvements (Optional)

Streaming responses

Chat history

Dark mode

Online deployment

Mobile UI
