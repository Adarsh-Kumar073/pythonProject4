import pickle
import json
import os
import pandas as pd
import numpy as np

__model= None
__locations= None
__columns= None

def predict_price(location, sqft, bhk, bath):
    try:
        loc_index = __columns.index(location.lower())
    except ValueError:
        loc_index = -1
    x= np.zeros(len(__columns))
    x[0]=sqft
    x[1]=bath
    x[2]= bhk
    if loc_index >0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)

def load_artifacts():
    print('loading_artifacts_start....')
    global __columns
    global __locations

    artifacts_path= "artifacts"

    column_file= os.path.join(artifacts_path,'columns.json')
    model_file= os.path.join(artifacts_path,'banglore_home_prices_model.pickle')

    with open(column_file, 'r') as f:
        __columns= json.load(f)['data_columns']
        __locations=__columns[3:]

    global __model
    with open(model_file, 'rb') as fb:
        __model= pickle.load(fb)

    print('Loading artifacts done....')
def get_location_names():
    return __locations

def get_column_names():
    return __columns

if __name__ == '__main__':
    load_artifacts()
    print(get_location_names())
    print(predict_price('1st Phase JP Nagar', 1000, 3, 3))
    print(predict_price('1st Phase JP Nagar', 1000, 2, 2))
    print(predict_price('Kalhalli', 1000, 2, 2))  # other location
    print(predict_price('Ejipura', 1000, 2, 2))  # other location

