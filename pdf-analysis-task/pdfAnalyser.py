import os
from pypdf import PdfReader
from dotenv import load_dotenv
from mistralai.client import Mistral


load_dotenv()

# INTIALIZING 
apiKey = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"
client = Mistral(api_key=apiKey)
pdfPath = "Python Reference Manual.pdf"

# EXTRACTING PDF TEXT
reader = PdfReader(pdfPath)
pdfText = ""

# LOOPING THROUGH THE PAGES 
for page in reader.pages:
    pdfText += page.extract_text()

# NOW EXTRACTION IS COMPLETE AND IT'S SENT TO AI

# INITIAL CONTEXT
messages = [
{"role": "system", "content": "You are an AI assistant analyzing a Python Reference Manual for the user."},
{"role": "user", "content": f"Here is the text we will discuss:\n\n{pdfText}\n\nAcknowledge that you read it and are ready to answer my questions."}
]  # here "system" is used first to give the initial set of instructions
   # it sets the rules, persona and boundaries for the AI
   # once the AI knows its job description, user provides actual input it needs to process

# INITIAL ACKNOWLEDGEMENT FROM AI 
response = client.chat.complete(model = model, messages = messages)
aiReply = response.choices[0].message.content
print(f"AI: {aiReply}")

# SAVING AI REPLY TO CHAT HISTORY
messages.append({"role": "assistant", "content": aiReply})

print("The document has loaded. Type 'exit' to leave the session.\n")

while True:
    userInput = input("You: ")

    if userInput.lower() == "exit":
        print("Ending session..")
        break

    # ADDING USER'S NEW QUESTION TO HISTORY
    messages.append({"role": "user", "content": userInput})

    # SENDING UPDATED HISTORY TO AI
    response = client.chat.complete(model = model, messages = messages)
    reply = response.choices[0].message.content
    print(f"AI: {reply}")

    # APPENDING AI'S REPLY SO ITS REMEMBERED FOR NEXT LOOP
    messages.append({"role": "assistant", "content": reply})


