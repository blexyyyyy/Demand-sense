DemandSense is an end-to-end machine learning system that forecasts weekly store sales using real Walmart retail data.
It includes a full ML pipeline: data cleaning, feature engineering, time-based splitting, model training (RandomForest/XGBoost), and a Streamlit web dashboard for live forecasting.

This is a production-style forecasting project designed to demonstrate real ML engineering skills beyond simple notebooks.

Features

🔹 Full ML Pipeline

Cleaned + validated real retail sales data

Created time-based features (week, month, year, lags, rolling stats)

Global model trained across 45 stores

Proper time series split (train: 80%, validation: 20%)


🔹 Models Trained

Naive Lag-1 baseline

RandomForest Regressor (best model)

XGBoost Regressor


Best Model Performance (Random Forest):

MAE: 57,919

RMSE: 98,301

MAPE: 5.09%


🔹 Deployment

A fully interactive Streamlit dashboard where users can:

Select a store

Choose a forecast horizon (1–12 weeks)

View historical sales

View predicted future sales

Download forecast results



---

🧱 Project Structure

demandsense/
├── app/
│   └── streamlit_app.py
├── data/
│   ├── raw/           # ignored by git
│   └── processed/     # ignored by git
├── models/            # ignored by git
├── notebooks/
│   ├── 01_eda_cleaning.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_modeling.ipynb
├── src/
├── requirements.txt
└── README.md


---

🧠 Technical Highlights

Feature Engineering

Lag features: lag_1, lag_2, lag_4

Rolling statistics: roll_mean_4, roll_std_4, roll_mean_8

Time features: year, month, week, day_of_week, etc.

Global modeling across all stores (more robust, more data)


Why a Global Model?

Store-level data is too small alone (~50 rows), so a global model across all 45 stores was used — a real forecasting best practice.


---

📊 Streamlit App Screenshots

(Add 1–2 screenshots once you take them)


---

📦 Installation

Create a virtual environment:

python -m venv .venv

Activate it:

.\.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt


---

▶️ Run the App

From project root:

streamlit run app/streamlit_app.py

