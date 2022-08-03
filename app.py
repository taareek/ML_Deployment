# importing necessary libraies 
import uvicorn 
from fastapi import FastAPI
from BankNotes import BankNote
import pickle 
import pandas as pd

# create the app object 
app = FastAPI()

# getting pickle file 
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

# home route
@app.get("/")
def home():
    return {"message": "Hola!! como estas?"}

# greetings route by name 
@app.get("/greet/{name}")
def get_greetings(name: str):
    return {"grettings": "La bienvenidas "+f'{name}'}

# prediction for Bank note authentication 
# Expose the prediction functionality, make a prediction from the passed parameters (values)
# JSON data and return the predicted Bank Note with the confidence
@app.post("/prediction")
def get_prediction(data:BankNote):
    # converting data as a dictionary
    data = data.dict()

    # taking feature wise data
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']

    # predict 
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print("The predicted value is: ", prediction)

    # performing binary classification for fake note and bank note 
    if(prediction[0] > 0.5):
        prediction = 'Fake note'
    else:
        prediction = "Bank note"
    
    return {
        'prediction': prediction
    }

# Run the API with uvicorn 
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
