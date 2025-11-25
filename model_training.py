
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the preprocessed data
try:
    X_train = pd.read_csv("X_train_preprocessed.csv")
    X_test = pd.read_csv("X_test_preprocessed.csv")
    y_train = pd.read_csv("y_train.csv").values.ravel()
    y_test = pd.read_csv("y_test.csv").values.ravel()
except FileNotFoundError as e:
    print(f"Error loading data: {e}")
    print("Please run data_preprocessing.py first.")
    exit()

# Initialize and train the model
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(model, 'churn_model.pkl')
print("\nModel training complete and model saved as churn_model.pkl")
