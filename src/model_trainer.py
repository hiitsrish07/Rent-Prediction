from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
import joblib

def train_and_save_model(X, y, save_path="rent_model.pkl"):
    preprocessor = ColumnTransformer([
        ("loc_enc", OneHotEncoder(handle_unknown='ignore'), ["location"])
    ], remainder='passthrough')

    model = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    model.fit(X, y)
    joblib.dump(model, save_path)
