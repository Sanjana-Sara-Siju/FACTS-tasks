# Conversational PDF Analyzer
A command-line Python application that leverages the Mistral AI API and `pypdf` to extract text from PDFs and allows users to interactively chat with the document's content.

## Features
* Uses pypdf to automatically parse and extract text from multi-page PDF documents.
* Maintains conversation history so the AI remembers previous questions and answers during the session.
* Utilizes `python-dotenv` to ensure API keys remain completely isolated from the source code.

## Prerequisites
* A **Mistral AI** API Key

## Installation

1. **Clone the repository and switch to the task branch:**
  
   git clone <your-repository-url>

   cd data-extraction-task/pdf-analysis-task

   git checkout pdf-analysis-task

2. **Set up a virtual environment:**

.\venv\Scripts\Activate.ps1

3. **Install the required dependencies:**

pip install pypdf mistralai python-dotenv 

4. **Environment Setup:**

Create a .env file in the root directory of this task and add your Mistral API key:

MISTRAL_API_KEY=your_actual_key_here

Note : Ensure your .gitignore is configured to ignore the .env file

5. **Add your document**

Place the PDF you wish to analyze into the folder and update the pdfPath variable in the script if necessary.

6. **Running the script**

Run the script from your active virtual environment:

python pdfAnalyser.py

Wait for the AI to acknowledge the document, and then begin typing your questions in the interactive terminal prompt. Type 'exit' to end the session.


