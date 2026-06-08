# Gmail API - Sending a simple email
This project contains a Python script (`sendEmail.py`) designed to automate the transmission of plain-text emails utilizing the Google Workspace Gmail API. The utility handles secure OAuth 2.0 user authentication, local token management via serialization, and message encoding required by Google's API endpoints.


## Features
* OAuth 2.0 Authentication prompts user authorization and securely stores refresh/access tokens locally.
* Automatically checks for existing `token.pickle` sessions to bypass redundant browser logins.
* Base64 encoding formats `MIMEText` objects into the URL-safe Base64 strings required by the Gmail API.
* Executes the API command to send targeted emails directly from the authenticated user's outbox.

## Prerequisites
* Python 3.x installed.
* A registered Google Cloud Platform (GCP) project with the **Gmail API** enabled.
* An OAuth 2.0 Client ID (Desktop Application) configured within the GCP Google Auth Platform.
* The target sender/recipient email addresses must be whitelisted in the GCP "Test users" section while the app is in Testing mode.

## Setup & Installation

1. **Clone the repository:**

Navigate to your project directory and clone the repository.
  
git clone <repository-url>

cd gmail-api-task

2. **Establish a virtual environment:**

It is highly recommended to isolate the Google API dependencies.

python -m venv venv

venv\Scripts\activate

3. **Install required libraries:**

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

4. **Configure credentials:**

Download the OAuth Client ID credentials.json file from the Google Cloud Console.

Place credentials.json directly into the root directory of this project.

## How to Test

Execute the script from the terminal:

python sendEmail.py

Initially, the script will pause and open a web browser requesting Google account authorization. Once granted, it generates a token.pickle file in the root directory and dispatches the test email.

Subsequent Runs:

The script will silently authenticate using token.pickle and immediately dispatch the email without launching a browser.

**NOTE:** Do not commit API credentials or session tokens to version control. Ensure your .gitignore file includes the following entries prior to staging any commits:

credentials.json
token.pickle
venv/

