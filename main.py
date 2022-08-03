# importing libraies
import uvicorn   #ASGI
from fastapi import FastAPI

# creating app object
app = FastAPI()

# home route
@app.get("/")

def home():
    return {"message": "Hola !! como estas?"}

# another route
@app.get("/welcome")

def get_grettings(name:str):
    return {"Welcome":"La bienvenidas "+f'{name}'}

# to run the app in the localhost server we need use this comman 
# uvicorn main:app --reload => where main is the file name and app is our app name 
# now we write a condition statement to run this script

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)