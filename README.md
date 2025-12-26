<<<<<<< HEAD
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

=======
DemandSense — Retail Sales Forecasting, Built the Right Way

Retail businesses live and die by one question:
“How much will we sell next week?”

DemandSense is my answer to that.

This project is an end-to-end ML system that forecasts weekly Walmart store sales.
I didn’t treat this like a toy notebook — I built it like a real ML engineer would:

cleaned messy real-world data

engineered meaningful time-series features

trained multiple models

compared them honestly

deployed an interactive forecasting app


If your goal is to understand whether I can build practical ML systems, this project should make it very clear.


---

🚀 What DemandSense Actually Does

Learns sales patterns from 45 Walmart stores

Builds a global forecasting model (more realistic than store-by-store)

Predicts future weekly sales for any store you select

Lets you choose 1–12 week forecast horizons

Shows the forecast on a clean Streamlit dashboard

Lets you download predictions for further analysis


It's simple enough to use, but powerful under the hood.


---

🧠 Why I Built It (The Intent Behind the Project)

Time-series forecasting is everywhere — retail, logistics, finance, agriculture.
I wanted a project that shows:

I can handle real data, not sanitized samples

I understand what features matter in forecasting

I can build and evaluate models honestly

I can deploy ML in a UI that non-technical people can use

I can structure a project like someone who’s done this before


So DemandSense became my “prove it” project.


---

📊 Model Performance (No Hype, Just Results)

Out of all models, RandomForest performed best:

Model	MAE	RMSE	MAPE

Naive Lag-1	88,276	305,567	97.9%
RandomForest	57,919	98,301	5.09%
XGBoost	64,364	75,492	5.89%


The takeaway:
A simple, well-tuned RandomForest beat everything else.

🖥️ The Dashboard (What users see)

The Streamlit app lets you:

Pick a store

Pick a forecast horizon

See full historical trends

See your future sales curve

Download forecast as CSV


It’s smooth, visual, and built for actual decision makers — not just ML folks.


---

⚙️ Run It Yourself

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app/streamlit_app.py



That's real ML — not every problem needs deep learning.

>>>>>>> b15ad37f4f5f9d21fdb6e97c5384d8a9ea54e3bc
