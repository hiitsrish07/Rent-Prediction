import pandas as pd
import joblib

def load_model(path="rent_model.pkl"):
    return joblib.load(path)

def predict_rent(model, bhk, location):
    input_df = pd.DataFrame([[bhk, location]], columns=["bhk", "location"])
    return model.predict(input_df)[0]
