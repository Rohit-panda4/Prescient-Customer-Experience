import pandas as pd
import requests
import io

def get_data():
    """
    Downloads the Telco Customer Churn dataset from a public URL and returns it as a pandas DataFrame.
    """
    url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        df = pd.read_csv(io.StringIO(response.text))
        return df
    except requests.exceptions.RequestException as e:
        print(f"Error downloading data: {e}")
        return None

if __name__ == '__main__':
    data = get_data()
    if data is not None:
        data.to_csv("churn_data.csv", index=False)
        print("Data ingested and saved to churn_data.csv")
