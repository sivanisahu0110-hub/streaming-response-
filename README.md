 # Streaming Responses Demo

## Project Overview

This project demonstrates how to implement real-time streaming responses using the Google Gemini API and FastAPI.

The application accepts a user prompt, sends it to the Gemini Large Language Model (LLM), receives the generated response as a stream, and returns it to the client using FastAPI's `StreamingResponse`.

---

## Features

* FastAPI REST API
* Google Gemini API integration
* Real-time streaming responses
* Environment variable support using `.env`
* Simple and modular project structure

---

## Technologies Used

* Python
* FastAPI
* Google Gemini API (`google-genai`)
* Uvicorn
* python-dotenv

---

## Project Structure

```text
streaming-response/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

1. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

4. Run the application:

```bash
uvicorn app.main:app --reload
```

5. Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## How It Works

1. The user enters a prompt.
2. FastAPI sends the prompt to the Gemini model.
3. Gemini generates the response as a stream.
4. The application processes the streamed response and returns it using `StreamingResponse`.

---

## Future Improvements

* Integrate with the main LLM module.
* Add a frontend interface for live streaming.
* Improve UI and user experience.

---

## Author

**Sivani Sahu**

