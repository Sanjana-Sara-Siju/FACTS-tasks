import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict
import pypdf
import io # provides memory buffer handlers
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

#initializing Mistral Client 
apiKey = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"
client = Mistral(api_key = apiKey)

#Pydantic model to receive full chat history from frontend
#specifies the exact type mapping expected from frontend request: a JSON object containing a messages key mapped to an array of objects
class ChatHistoryRequest(BaseModel):
    messages: List[Dict[str, str]]

#binds landing route directly to the server root URL
@app.get("/", response_class = HTMLResponse) #reads index.html and sends it to browser
async def serve_frontend():
    with open("index.html", "r") as f:
        return f.read()
    
#route --> extracts PDF text dynamically 
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_bytes = await file.read() #converts stream directly into raw binary data
    extracted_text = ""
    
    if file.filename.endswith(".pdf"):
        pdf_reader = pypdf.PdfReader(io.BytesIO(file_bytes)) #feeds binary bytes in memory to pypdf as if it were an opened file
        for page in pdf_reader.pages:
            extracted_text += page.extract_text() or ""  #loops through all pages, grabs the characters and glues them into 1 continuous string block
    elif file.filename.endswith(".txt"):
        extracted_text = file_bytes.decode("utf-8")
    else:
        return {"error": "Unsupported file type. Please upload a .txt or .pdf."}

    return {"filename": file.filename, "text": extracted_text}


#route --> continuous chat endpoint matching prev conversation logic
@app.post("/chat")
async def chat_with_pdf(request: ChatHistoryRequest):
    try:
        #sends entire accumulated message history to Mistral AI
        response = client.chat.complete(
            model = model, 
            messages = request.messages
        )
        ai_reply = response.choices[0].message.content
        return {"reply": ai_reply}
        
    except Exception as e:
        return {"error" : "Failed to communicate with Mistral AI"}


