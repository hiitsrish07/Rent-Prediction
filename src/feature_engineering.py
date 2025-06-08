def preprocess_features(df):
    X = df[["bhk", "location"]]
    y = df["rent"]
    return X, y