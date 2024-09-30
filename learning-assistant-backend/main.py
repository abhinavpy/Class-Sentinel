# main.py
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class GuardrailsRequest(BaseModel):
    settings: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    student_message = request.message
    # For now, we'll return a simple echo response
    reply = f"Echo: {student_message}"
    return {"reply": reply}

@app.post("/guardrails")
async def guardrails_endpoint(request: GuardrailsRequest):
    # Save the guardrails settings (you can save to a file or database)
    with open('guardrails.txt', 'w') as f:
        f.write(request.settings)
    return {"message": "Guardrails saved successfully."}

@app.post("/upload")
async def upload_endpoint(file: UploadFile = File(...)):
    # Save the uploaded file
    file_location = f"uploaded_files/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())
    return {"message": f"File '{file.filename}' uploaded successfully."}
