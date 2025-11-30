
import pandas as pd
import joblib

# Load the trained model and preprocessor
print("Loading the trained model and preprocessor...")
model = joblib.load('churn_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')
print("Model and preprocessor loaded.")

# Load the raw customer data
print("Loading customer data...")
df = pd.read_csv('churn_data.csv')
print("Data loaded.")

# Separate features for prediction (all columns except 'customerID' and 'Churn')
X_new = df.drop(["customerID", "Churn"], axis=1)


# Preprocess the new data
print("Preprocessing new data...")
X_new_preprocessed = preprocessor.transform(X_new)
print("Data preprocessed.")

# Convert the preprocessed data to a dense array
X_new_preprocessed_dense = X_new_preprocessed.toarray()


# --- Generate Predictions ---
print("Generating churn predictions...")
# Predict the probability of churn
churn_probabilities = model.predict_proba(X_new_preprocessed_dense)[:, 1]

# Add the predictions back to the original dataframe
df['ChurnProbability'] = churn_probabilities

# Classify customers as High, Medium, or Low risk
def assign_risk_level(prob):
    if prob > 0.7:
        return 'High Risk'
    elif prob > 0.4:
        return 'Medium Risk'
    else:
        return 'Low Risk'

df['RiskLevel'] = df['ChurnProbability'].apply(assign_risk_level)
print("Predictions generated.")


# --- Save the Final CSV for Power BI ---
output_filename = 'customer_churn_predictions.csv'
df.to_csv(output_filename, index=False)
print(f"\nSuccessfully generated predictions! The data is saved in '{output_filename}'.")
print("You can now connect this file to Power BI.")
