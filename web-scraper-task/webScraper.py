import os
import requests
from bs4 import BeautifulSoup
from google import genai
from dotenv import load_dotenv

# LOADING API KEY
load_dotenv() # reading hidden .env file
client = genai.Client() # automatically grabs API key 

url = "https://a2a-protocol.org/latest/topics/key-concepts/"

# FETCHING THE WEBPAGE
response = requests.get(url)

if response.status_code == 200: #successful HTTP request
    soup = BeautifulSoup(response.content, 'html.parser') 
    #converting raw HTML data into structured Python object

    # web elements not required
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.extract()

    # exracting the text 
    raw_text = soup.get_text(separator = ' ', strip = True)

    # sending clean text to Gemini to summarize
    prompt = "Summarize the following scraped webpage text into a brief and easy-to-read format." \
             " Explain the key concepts using bullet points."
    
    result = client.models.generate_content(model = 'gemini-2.5-flash',contents = [prompt, raw_text])

    # SAVING SUMMARY TO A TEXT FILE 
    with open('summary.txt', 'w') as file:
        file.write(result.text)

    print("Summary saved in summary.txt.")

else:
    print("Failed to retrieve webpage")

    


    
