from fastapi import FastAPI
from fastapi.responses import RedirectResponse
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/owner")
def read_owner():
    return {"message": "This API Belong to Priyanka Koul.....😀"}

@app.get("/github")
def redirect_to_github():
    return RedirectResponse(url="https://github.com/PriyankaKoul001/first-fastapi-with-frontend")

@app.get("/linkedin")
def redirect_to_linkedin():
    return RedirectResponse(url="https://www.linkedin.com/in/priyanka-koul-a5b1a5361/")