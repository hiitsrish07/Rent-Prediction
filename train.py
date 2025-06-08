from src.data_loader import load_and_clean_data
from src.feature_engineering import preprocess_features
from src.model_trainer import train_and_save_model

def main():
    # Load and clean the dataset
    df = load_and_clean_data("rent_data.csv")
    print("Shape of DataFrame:", df.shape)
    print("DataFrame sample:\n", df.head())

    # Prepare features and target variable
    X, y = preprocess_features(df)

    # Train the model and save it as rent_model.pkl
    train_and_save_model(X, y, save_path="rent_model.pkl")
    print("✅ Model trained and saved to rent_model.pkl")

if __name__ == "__main__":
    main()
