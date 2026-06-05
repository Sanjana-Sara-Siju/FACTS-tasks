# FastAPI Login, SIgnup and Calculator Web Application
A simple, interactive web application built with Python and FastAPI. This project demonstrates a complete user flow: creating an account with validation constraints, logging in, and using a functional calculator.

## Features
* Users can create an account. Passwords are strictly validated using Pydantic Base Models to ensure they are a minimum of 8 characters long.
* Authenticates returning users against a mock database and securely redirects them upon successful entry.
* A fully functional calculator (Add, Subtract, Multiply, Divide) that processes input and dynamically renders the result on the same page.
* Form based submission fully compatible with standard HTML web forms and Postman (`x-www-form-urlencoded`).

## Tech Stack
* **Backend Framework:** FastAPI
* **Data Validation:** Pydantic (BaseModel)
* **Templating Engine:** Jinja2
* **Server:** Uvicorn
* **Frontend:** HTML5

## 📁 Project Structure

web-app-task/

├── main.py       
        # Core application logic and routing
├── README.md     

└── templates/    
        # Directory containing HTML files
    ├── signup.html      

    ├── login.html     

    └── calculator.html   

## Installation and Setup
1. **Clone the repository and switch to the task branch:**

git clone <your-repo-link>
cd web-app-task

2. **Install the required dependencies:**

pip install fastapi uvicorn pydantic jinja2 python-multipart

3. **Run the local development server:**

uvicorn main:app --reload

The application will be live at http://127.0.0.1:8000.

## How to Test
You can test this application locally using a standard web browser or via Postman.

**Testing via Web Browser**

Navigate to http://127.0.0.1:8000/signup.

Create an account (ensure your password is at least 8 characters or you will receive a validation error).

Upon successful creation, you will be redirected to the Login page.

Log in with your new credentials.

Upon successful login, you will be redirected to the Calculator page.

**Testing via Postman**

Note: Because this application uses HTML forms, you must send data using the x-www-form-urlencoded body type.

SIGN UP:

Method: POST | URL: http://127.0.0.1:8000/signup

Body: x-www-form-urlencoded

Keys: username, password (min 8 chars)

LOGIN:

Method: POST | URL: http://127.0.0.1:8000/login

Body: x-www-form-urlencoded

Keys: username, password

CALCULATOR:

Method: POST | URL: http://127.0.0.1:8000/calculator

Body: x-www-form-urlencoded

Keys: num1 (number), num2 (number), operation (value: "add", "subtract", "multiply", or "divide")

The calculated result will be injected directly into the returned HTML response.
