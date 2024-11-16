from fastapi import FastAPI, HTTPException
import joblib
model = joblib.load('xgboost_model_sklearn.pkl')
scaler = joblib.load('scaler.joblib')
app = FastAPI()
# GET request
@app.get("/")
def read_root():
    return {"message": "Welcome to Tuwaiq Academy"}
# get request
@app.get("/items/")
def create_item(item: dict):
    return {"item": item}

from pydantic import BaseModel
# Define a Pydantic model for input data validation
class InputFeatures(BaseModel):
    goals: float
    assists: float
    minutes_played: int
    games_injured: int
    award: int
    highest_value: int

def preprocessing(input_features: InputFeatures):
    dict_f = {
    'goals': input_features.goals,
    'assists': input_features.assists,
    'minutes played': input_features.minutes_played,
    'games_injured': input_features.games_injured,
    'award': input_features.award,
    'highest_value': input_features.highest_value
    }
    # Convert dictionary values to a list in the correct order
    features_list = [dict_f[key] for key in sorted(dict_f)]
    # Scale the input features
    scaled_features = scaler.transform([list(dict_f.values())])
    return scaled_features


@app.get("/predict")
def predict(input_features: InputFeatures):
    return preprocessing(input_features)

@app.post("/predict")
async def predict(input_features: InputFeatures):
    data = preprocessing(input_features)
    y_pred = model.predict(data)
    return {"pred": y_pred.tolist()[0]}
