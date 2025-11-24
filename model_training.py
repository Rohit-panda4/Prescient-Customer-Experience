import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

def train_model():
    df = pd.read_csv("churn_data.csv")

    # Example feature engineering - replace with your own
    df['tenure_group'] = pd.cut(df['tenure'], bins=[0, 12, 24, 36, 48, 60, 72], labels=['0-1', '1-2', '2-3', '3-4', '4-5', '5-6'])

    # Select features and target
    features = ['tenure', 'monthly_charges', 'total_charges']  # Replace with your features
    target = 'churn'  # Replace with your target variable

    X = df[features]
    y = df[target]

    # Handle missing values (if any)
    X = X.fillna(X.mean())

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))

    # Save the model
    joblib.dump(model, 'churn_model.pkl')
    print("Model trained and saved to churn_model.pkl")

if __name__ == '__main__':
    train_model()
