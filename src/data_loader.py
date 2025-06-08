import pandas as pd
import re

def load_and_clean_data(csv_path):
    df = pd.read_csv(csv_path)
    print("Columns in CSV:", df.columns.tolist())

    

    # Clean the rent column: remove ₹, commas, and handle newline cases
    df["rent"] = df["rent"].astype(str)
    df["rent"] = df["rent"].str.replace(r"[^\d.]", "", regex=True)  # Remove ₹, commas, newlines, etc.
    df["rent"] = pd.to_numeric(df["rent"], errors="coerce")

    # Clean BHK column: extract number from '2 BHK', '1 RK', etc.
    df["bhk"] = df["bhk"].astype(str)
    df["bhk"] = df["bhk"].str.extract(r"(\d+)").astype(float)

    # Drop rows with any missing critical data
    df = df.dropna(subset=["rent", "bhk","location"])

    return df
