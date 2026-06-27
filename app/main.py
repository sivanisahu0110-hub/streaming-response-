from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from google import genai
import time


from app.config import GEMINI_API_KEY
# create fastapi app
app = FastAPI(
    title="Streaming Responses Demo",
    version="1.0.0"
)

#gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Stream response generator
def generate_stream(prompt: str):
    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    counter = 0


    for chunk in response:
        if chunk.text:
            for word in chunk.text.split():
               print(f"streaming token: {word}")
            yield f": {word}"
            time.sleep(0.05)  # Simulate delay for streaming effect
            
# Stream response endpoint
@app.post("/stream")
def stream_response(prompt: str):
    return StreamingResponse(
        generate_stream(prompt),
        media_type="text/event-stream"
    )