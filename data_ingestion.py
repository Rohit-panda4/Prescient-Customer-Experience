import pandas as pd
import psycopg2

def get_data():
    # Replace with your actual database credentials
    conn = psycopg2.connect(
        host="your_host",
        database="your_database",
        user="your_user",
        password="your_password"
    )

    # Example query - replace with your actual queries
    user_demographics_query = "SELECT * FROM user_demographics"
    usage_history_query = "SELECT * FROM usage_history"

    user_demographics = pd.read_sql(user_demographics_query, conn)
    usage_history = pd.read_sql(usage_history_query, conn)

    conn.close()

    # Merge the dataframes
    df = pd.merge(user_demographics, usage_history, on="user_id")

    return df

if __name__ == '__main__':
    data = get_data()
    data.to_csv("churn_data.csv", index=False)
    print("Data ingested and saved to churn_data.csv")
