from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import main
from pydantic import BaseModel

app= FastAPI()

@app.on_event("startup")
def load_model_artifacts():
    main.load_artifacts()

@app.get('/get_location_names')
def get_location_names():
    locations= main.get_location_names()
    return {'locations':locations}

class PricePredictionRequest(BaseModel):
    location: str
    total_sqft: float
    bhk: int
    bath: int

@app.post('/predict_home_price')
async def predict_home_price(request: PricePredictionRequest):
    location = request.location
    total_sqft = request.total_sqft
    bhk = request.bhk
    bath = request.bath

    estimated_price = main.predict_price(location, total_sqft, bhk, bath)

    return {'estimated_price': estimated_price}



if __name__=='__main__':
    print('Everything is fine')
    main.load_artifacts()
    print(main.predict_price('1st Phase JP Nagar', 1000, 3, 3))


