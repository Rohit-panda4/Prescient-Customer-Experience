import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('churn_model.pkl')

# Load the data
df = pd.read_csv('churn_data.csv')

# Set the title of the dashboard
st.title("The Churn Shield")

# Add a sidebar for filtering
st.sidebar.header("Filter Customers")

# Example filter - by tenure
tenure = st.sidebar.slider("Tenure (months)", 0, 72, (0, 72))

# Filter the data based on the selection
filtered_df = df[(df['tenure'] >= tenure[0]) & (df['tenure'] <= tenure[1])]

# Predict churn probability for the filtered customers
features = ['tenure', 'monthly_charges', 'total_charges'] # Make sure these match the training script
filtered_df = filtered_df.fillna(filtered_df[features].mean())
filtered_df['churn_probability'] = model.predict_proba(filtered_df[features])[:, 1]

# Identify high-risk customers
filtered_df['risk_level'] = pd.cut(filtered_df['churn_probability'], bins=[0, 0.5, 1], labels=["Low Risk", "High Risk"])

# Display the high-risk customers
st.subheader("High Risk Customers")
st.dataframe(filtered_df[filtered_df['risk_level'] == "High Risk"])

# Allow downloading the high-risk customer list
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(filtered_df[filtered_df['risk_level'] == 'High Risk'])

st.download_button(
    label="Download High-Risk Customers as CSV",
    data=csv,
    file_name='high_risk_customers.csv',
    mime='text/csv',
)
