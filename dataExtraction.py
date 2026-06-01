import json
import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("--image", type=str)
parser.add_argument("--output", type=str, default = "output.json")
args = parser.parse_args() # grabbing input from terminal
# after this you can pull image path by calling args.image and output path 
# by calling args.output

# LOADING API KEY
load_dotenv() # reading hidden .env file
client = genai.Client() # automatically grabs API key 

# LOADING IMAGE USING PILLOW
img = Image.open(args.image)

prompt = "You are an expert data analyist. Look at the attached interview cover sheet. " \
"Extract just the interviewee's details and return them matching the following JSON format. " \
"If a field is empty, return 'null' for that field. " \
"{" \
"   name: Interviewee's full name," \
"   gender: Interviewee's gender, " \
"   email address: Interviewee's email address, " \
"   mobile number: Interviewee's mobile number, " \
"   date of birth: Interviewee's date of birth, " \
"   age: Interviewee's age in years, " \
"   marital status: Interviewee's marital status, " \
"   no of kids: Interviewee's number of kids if any, " \
"   current visa: Interviewee's type of visa, " \
"   visa validity: Interviewee's visa validity date, " \
"   final qualification with specialisation: Interviewee's qualification, " \
"   year of course completion/name of institution: Interviewee's completion year/name of institution, " \
"   work experience in uae: Interviewee's work experience in UAE in years, " \
"   work experience in india/other countries: Interviewee's work experience in other countries in years, " \
"   main software platforms worked: Interviewee's software platforms worked, " \
"   academic_years: [List of years of passing from the table], " \
"   academic_marks: [List of % marks obtained from the table]" \
"}"

# TO GET JSON OUTPUT
response = client.models.generate_content(model = 'gemini-2.5-flash', contents = [prompt, img], config = types.GenerateContentConfig(response_mime_type = "application/json"))


# CONVERTING RESPONSE TEXT BACK INTO PYTHON 
extractedData = json.loads(response.text) 


# SAVING RESULTS INTO JSON FILE
with open(args.output, 'w') as json_file:
    json.dump(extractedData, json_file, indent = 4)

print(f"\nData succesfully saved into {args.output}")



    








