from fastapi import FastAPI, Request, Form  # Form --> to test via Postman and HTML forms 
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field, ValidationError # pydantic base model 

app = FastAPI() # to initialize the FastAPI app
templates = Jinja2Templates(directory = "templates") # tells app where HTML files are located
db_users = {} # to store user data , to check if username and password are matching

# PYDANTIC MODELS

# defines expected structure for a user signing up 
class User(BaseModel):
    username: str
    password: str = Field(min_length = 8) # as per constraint 

# makes sure calculator receives 2 nos and an operation
class Calc(BaseModel):
    num1: float
    num2: float
    operation: str

# SIGN UP

# when you type a http://.../signup in browser, it serves a blank HTML page
@app.get("/signup")
def get_signup(request: Request):
    return templates.TemplateResponse(request = request, name = "signup.html")

# catches the data when Submit is clicked or SEND in Postman 
# Forn(...) forces it to look for form data
@app.post("/signup")
def post_signup(request: Request, username: str = Form(...), password: str = Form(...)):
    try:
        user = User(username = username, password = password) 
        db_users[user.username] = user.password # key value pair kind of 
        return RedirectResponse("/login", status_code = 303) # redirecting user to login page
    except ValidationError:
        return templates.TemplateResponse(
            request = request, 
            name = "signup.html", 
            context = {"error": "Password needs more than 8 characters."}
        )

# LOGIN

# serves blank login HTML page 
@app.get("/login")
def get_login(request: Request):
    return templates.TemplateResponse(request = request, name = "login.html")

# takes form data, looks up username in dictionary, and checks if password matches 
# if yes, it redirects the user to the calculator
@app.post("/login")
def post_login(request: Request, username: str = Form(...), password: str = Form(...)):
    if db_users.get(username) == password:
        return RedirectResponse("/calculator", status_code = 303)
    return templates.TemplateResponse(
        request = request, 
        name = "login.html", 
        context = {"error": "Wrong username and password.."}
    )

# CALCULATOR

# serves blank calculator HTML page 
@app.get("/calculator")
def get_calc(request: Request):
    return templates.TemplateResponse(request = request, name = "calculator.html") 

# Calc pydantic model for validation
@app.post("/calculator")
def post_calc(request: Request, num1: float = Form(...), num2: float = Form(...), operation: str = Form(...)):
    try:
        data = Calc(num1 = num1, num2 = num2, operation = operation)
        
        # dictionary that does the math based on what operation the user chose in the dropdown menu
        math = {
            "add": data.num1 + data.num2,
            "subtract": data.num1 - data.num2,
            "multiply": data.num1 * data.num2,
            "divide": data.num1 / data.num2 if data.num2 != 0 else "Cannot divide by 0"
        }
        
        # reloads the same calculator.html template, but this time injects a new variable named result into the page
        return templates.TemplateResponse(
            request = request, 
            name = "calculator.html", 
            context = {"result": math[data.operation]}
        )
    
    except ValidationError:
        return templates.TemplateResponse(
            request = request, 
            name = "calculator.html", 
            context = {"error": "Invalid numbers.."}
        )