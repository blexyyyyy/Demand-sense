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

