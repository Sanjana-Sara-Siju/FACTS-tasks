# PDF Upload & AI PDF Conversational Analysis Web App
An interactive, conversational chat web application built using FastAPI and the Mistral AI API. This application allows users to upload local ".pdf" or ".txt" files, extracts their text contents, and provides a formatted chat interface to converse with the document using historical context management.

## Features
- Using JavaScript and FastAPI and extracts structural text directly from PDFs and text files on-upload without refreshing the page.
- Manages a rolling conversational payload (system, user, and assistant roles) to ensure context preservation across sequential prompts.
- Integrates "Marked.js" on the frontend to parse raw AI markdown chunks into readable HTML elements (code blocks, bold text, bullet points).
- Hardened configuration utilizing a .gitignore mapping for environment arrays (.env) to prevent API key exposure.

## Tech Stack 
- **Backend Framework**: FastAPI (Python)
- **AI Orchestration**: Mistral Client API
- **Document Parsing**: PyPDF
- **Frontend Layer**: HTML5, JavaScript (Async/Await Fetch API), CSS
- **Markdown Parser**: Marked.js

## Installation & Local Setup

1. **Clone the Repository**

git clone <your-repository-url>

cd <repository-folder>

2. **Configure Your virtual environment**

python -m venv venv

# On Windows:

.\venv\Scripts\activate

3. **Install required dependencies**

pip install -r requirements.txt

pip install fastapi uvicorn python-multipart pypdf mistralai python-dotenv

4. **Environment setup**

Create a .env file in the root directory and append your secure client credentials:

MISTRAL_API_KEY=your_actual_api_key_here

5. **Run the local development server:**

uvicorn main:app --reload

Navigate to http://127.0.0.1:8000 in your web browser.

## Deployment Configuration (using Render)

This repository is configured to deploy directly to Render via continuous integration:
* Environment Targeting: Deployed from the development branch fastapi-pdf-upload-task.
* Build Command: pip install -r requirements.txt
* Start Command: uvicorn main:app --host 0.0.0.0 --port 10000
* Production Environment Variables: MISTRAL_API_KEY 




