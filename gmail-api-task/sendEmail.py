import os # to check if your authentication token file (token.pickle) alr exists in your directory 
          # so you don't have to log in every time
import pickle # to save your authentication token after you log in the 1st time
# Gmail API utils
from googleapiclient.discovery import build # takes your credentials and 
                                            # actually constructs the Gmail API service
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from base64 import urlsafe_b64encode # Gmail API cannot read standard Python strings directly. This encodes your email into a web-safe format that Google's servers can process.
from email.mime.text import MIMEText # used to write your email message 
                                     # (the subject,"To","From", and body)



# request all access (permission to read/send/receive emails, manage the inbox, and more)
SCOPES = ['https://mail.google.com/']
our_email = 'sanjanasarasiju@gmail.com'

# function loading credentials.json, doing authentication with Gmail API and 
# returning a service object that can be used later 

def gmail_authenticate():
    creds = None

    # token.pickle is automatically generated the 1st time the script is run 
    # and successfully login
    if os.path.exists("token.pickle"): # token.pickle stores the user's access & refresh tokens
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    
    # if no valid credentials available, let user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port = 0)

        # saving credentials for next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials = creds)

# getting the Gmail API service
service = gmail_authenticate()

# This is basically reading the credentials.json and saving it to token.pickle 
# file after authenticating with Google in your browser, we save the token, 
# so the 2nd time we run the code, we shouldn't authenticate again.


# creates and sends a simple text email
def send_email(service, recipient, subject, body_text):
    # constructing email using MIMEtext
    message = MIMEText(body_text)
    message['to'] = recipient
    message['from'] = our_email
    message['subject'] = subject

    # encoding the message in base64 (Gmail API requirement)
    raw_message = urlsafe_b64encode(message.as_bytes()).decode()
    body = {'raw': raw_message}

    # executing send command
    try:
        sent_message = service.users().messages().send(
      userId="me",
      body = body
    ).execute()
        
        print("Success! Message sent\n")
        return sent_message
    
    except Exception as e:
        print("An error occurred...")
        return None
    
if __name__ == "__main__":
    print("Authenticating with Google...")
    gmail_service = gmail_authenticate()

    recipient_email = "shreyab.facts@gmail.com" 
    
    email_subject = "Gmail API Test"
    email_body = "Hi Shreya,\nThis is a test email sent from my Python script using the Gmail API.\nBest Regards,\nSanjana Sara Siju\n"
    
    print(f"Sending email to {recipient_email}...")
    send_email(gmail_service, recipient_email, email_subject, email_body)


