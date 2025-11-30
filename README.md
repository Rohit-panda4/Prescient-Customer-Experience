# Prescient-Customer-Experience

## 1. Purpose of the Project

This project leverages machine learning to predict customer churn, providing a powerful tool for businesses to proactively identify and retain at-risk customers. By analyzing historical data, the system builds a predictive model that can forecast which customers are likely to discontinue their service. This enables targeted interventions and personalized retention strategies, ultimately leading to improved customer loyalty and reduced revenue loss. The project also features business intelligence dashboards to visualize churn patterns and model performance, offering actionable insights for data-driven decision-making.

## 2. How to Utilize the Repository (Guide to Setup in VS Code)

This step-by-step guide will walk you through setting up and running the project on your local machine using Visual Studio Code.

### Prerequisites

*   **Python 3.x:** Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
*   **Git:** Git is required to clone the repository. If you don't have it, you can download it from [git-scm.com](https://git-scm.com/downloads).
*   **VS Code:** Download and install Visual Studio Code from [code.visualstudio.com](https://code.visualstudio.com/).

### Step-by-Step Approach

1.  **Clone the Repository:**
    *   Open VS Code and press `Ctrl+Shift+P` to open the Command Palette.
    *   Type `Git: Clone` and press Enter.
    *   Paste the repository URL: `https://github.com/Rohit_Divekar/Prescient-Customer-Experience.git` and choose a local directory to save the project.

2.  **Open the Project:**
    *   Once cloned, open the project folder in VS Code by navigating to `File > Open Folder`.

3.  **Install Dependencies:**
    *   Open the integrated terminal in VS Code (`Ctrl+``).
    *   Create a virtual environment to manage project dependencies:
        ```bash
        python -m venv venv
        ```
    *   Activate the virtual environment:
        *   **Windows:** `.\venv\Scripts\activate`
        *   **macOS/Linux:** `source venv/bin/activate`
    *   Install the required libraries from `requirements.txt`:
        ```bash
        pip install -r requirements.txt
        ```

4.  **Run the Project:**
    *   The `main.py` script is the entry point for the data processing and model training pipeline. To run it, execute the following command in the terminal:
        ```bash
        python main.py
        ```
    *   This will execute the following scripts in order:
        1.  `data_ingestion.py`: Downloads the dataset.
        2.  `data_preprocessing.py`: Cleans and prepares the data.
        3.  `model_training.py`: Trains the churn prediction model.
        4.  `generate_predictions.py`: Creates predictions based on the trained model.

5.  **View the Dashboard:**
    *   To visualize the results and model insights, run the Streamlit dashboard:
        ```bash
        streamlit run dashboard.py
        ```
    *   This will open a new tab in your web browser with an interactive dashboard.

## 3. Data Analysis

### What the File Contained

The project analyzes the **Telco Customer Churn** dataset, which contains information about a fictional telecom company's customers. The dataset includes a mix of categorical and numerical features, such as:

*   **Customer Demographics:** Gender, age range, and dependents.
*   **Account Information:** Tenure (how long they've been a customer), contract type, and payment method.
*   **Services Signed Up For:** Phone service, multiple lines, internet service, online security, and more.
*   **Churn:** The target variable, indicating whether the customer churned or not.

### What Approach the Project Uses to Analyze Data

The project follows a standard machine learning pipeline to analyze the data and build a predictive model:

1.  **Data Ingestion:** The `data_ingestion.py` script automatically downloads the dataset from a public repository.
2.  **Data Preprocessing:** The `data_preprocessing.py` script handles data cleaning, transformation, and feature engineering. This includes converting categorical variables into a numerical format that the model can understand.
3.  **Model Training:** The `model_training.py` script uses the preprocessed data to train a classification model (e.g., Logistic Regression, Random Forest) to distinguish between churning and non-churning customers.
4.  **Prediction Generation:** The `generate_predictions.py` script applies the trained model to new, unseen data to generate churn predictions.

### What Output We Have Obtained from It

The primary output of the project is a set of churn predictions, which are saved to a CSV file. These predictions identify customers who are at high risk of leaving, allowing the business to take proactive measures. Additionally, the `dashboard.py` script creates an interactive web-based dashboard using Streamlit, which visualizes:

*   **Key performance indicators (KPIs)** related to customer churn.
*   **Distributions of customer demographics** and service usage.
*   **Model performance metrics** such as accuracy, precision, and recall.
*   **Feature importance**, showing which factors are most influential in predicting churn.

## 4. Project by Rohit Divekar

This project was developed by Rohit Divekar.

> "Data is the new oil. It’s valuable, but if unrefined, it cannot really be used." — Clive Humby

This quote inspired me to develop this project, as it highlights the importance of refining raw data into actionable insights. This project is an attempt to do just that—transforming customer data into a strategic asset for business growth.
