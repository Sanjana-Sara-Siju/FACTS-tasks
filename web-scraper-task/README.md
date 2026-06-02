# AI Web Scraper
This folder contains a Python script that scrapes a webpage, cleans the HTML, and uses the Google Gemini API to generate a brief, easy-to-read summary of the key concepts.

## Features
* Uses BeautifulSoup for HTML parsing and data extraction
* Uses google-genai for AI summarisation using gimini-2.5-flash
* Uses python-dotenv for secure API key management  

## Setup Instructions

1. **Activate the virtual environment**

Ensure you are using the local virtual environment to manage dependencies.

   .\venv\Scripts\activate

2. **Installations**

pip install requests beautifulsoup4 google-genai python-dotenv

3. **API key configuration**

Create a .env file in this folder and add your Gemini API key:

GEMINI_API_KEY=your_api_key_here

4. **Run the script from terminal**

python webScraper.py

The script will fetch the target URL, process the text, and output the AI-generated results into a new file called summary.txt.

