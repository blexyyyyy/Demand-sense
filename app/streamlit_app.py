import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="DemandSense Forecasting", layout="wide")

import os

# ----------------------------
# LOAD MODEL & DATA
# ----------------------------
# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define paths relative to the script location
# app/ is a sibling of models/ and data/
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "walmart_global_rf.pkl")
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "processed", "walmart_global_features.csv")

@st.cache_resource
def load_model():
    model = joblib.load(MODEL_PATH)
    return model

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

model = load_model()
df = load_data()

# ----------------------------
# SIDEBAR
# ----------------------------
st.sidebar.header("Forecast Settings")

store_list = sorted(df["Store"].unique())
selected_store = st.sidebar.selectbox("Select Store:", store_list)

horizon = st.sidebar.slider("Forecast Horizon (weeks)", 1, 12, 4)

st.sidebar.write("---")
st.sidebar.write("Developed with ❤️ by veerat m ")


# ----------------------------
# FILTER STORE DATA
# ----------------------------
store_df = df[df["Store"] == selected_store].copy()
store_df = store_df.sort_values("Date")

# Currency Conversion Strategy:
# The model is trained on USD data. We must keep `store_df` in USD for accurate predictions.
# We will create separate DataFrames/Columns for display purposes in INR.
USD_TO_INR = 84.0

# Create a display version for the historical plot
store_df_inr = store_df.copy()
store_df_inr["Weekly_Sales"] = store_df_inr["Weekly_Sales"] * USD_TO_INR

st.title(f"📈 DemandSense — Store {selected_store} Forecast")

# ----------------------------
# PLOT HISTORY
# ----------------------------
st.subheader("Historical Weekly Sales (₹)")

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(store_df_inr["Date"], store_df_inr["Weekly_Sales"])
ax.set_title(f"Historical Sales — Store {selected_store} (₹ Rupees)")
ax.set_xlabel("Date")
ax.set_ylabel("Weekly Sales (₹ Crores)")
# Format Y-axis to show Crores
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/1e7:,.2f} Cr'))
st.pyplot(fig)

# ----------------------------
# FEATURE COLUMNS
# ----------------------------
feature_cols = [
    'Store','year','month','week','day_of_week','day_of_year','is_weekend',
    'Holiday_Flag','Temperature','Fuel_Price','CPI','Unemployment',
    'lag_1','lag_2','lag_4',
    'roll_mean_4','roll_std_4','roll_mean_8'
]

# ----------------------------
# FORECAST FUNCTION
# ----------------------------
def make_forecast(store_df, horizon):
    df_fc = store_df.copy()
    df_fc = df_fc.sort_values("Date")

    # Start from the last actual known date
    current_date = df_fc["Date"].iloc[-1]

    # Last known values for lags
    last_sales = df_fc["Weekly_Sales"].iloc[-1]
    lag1 = df_fc["lag_1"].iloc[-1]
    lag2 = df_fc["lag_2"].iloc[-1]
    lag4 = df_fc["lag_4"].iloc[-1]

    # Copy static features from the last row
    static = df_fc.iloc[-1][[
        "Holiday_Flag", "Temperature", "Fuel_Price",
        "CPI", "Unemployment"
    ]].to_dict()

    predictions = []

    for i in range(horizon):
        # Next date
        current_date = current_date + pd.Timedelta(weeks=1)

        # Build feature row
        feat = {
            "Store": selected_store,
            "year": current_date.year,
            "month": current_date.month,
            "week": current_date.isocalendar().week,
            "day_of_week": current_date.weekday(),
            "day_of_year": current_date.timetuple().tm_yday,
            "is_weekend": 1 if current_date.weekday() >= 5 else 0,
            "Holiday_Flag": static["Holiday_Flag"],
            "Temperature": static["Temperature"],
            "Fuel_Price": static["Fuel_Price"],
            "CPI": static["CPI"],
            "Unemployment": static["Unemployment"],
            "lag_1": last_sales,
            "lag_2": lag1,
            "lag_4": lag2,
            "roll_mean_4": np.mean([last_sales, lag1, lag2, lag4]),
            "roll_std_4": np.std([last_sales, lag1, lag2, lag4]),
            "roll_mean_8": np.mean([last_sales, lag1, lag2, lag4]),  # simple fallback
        }

        feat_df = pd.DataFrame([feat])
        pred = model.predict(feat_df)[0]

        # Save prediction
        predictions.append([current_date, pred])

        # Update lags for next iteration
        lag4 = lag2
        lag2 = lag1
        lag1 = last_sales
        last_sales = pred

    forecast_df = pd.DataFrame(predictions, columns=["Date", "Forecast"])
    return forecast_df
# ----------------------------
# RUN FORECAST
# ----------------------------
forecast_df = make_forecast(store_df, horizon)

# Create display version of forecast
forecast_df_inr = forecast_df.copy()
forecast_df_inr["Forecast"] = forecast_df_inr["Forecast"] * USD_TO_INR

st.subheader(f"🔮 Forecast for next {horizon} weeks")

# Format the forecast dataframe for better display
display_df = forecast_df_inr.copy()
display_df["Forecast"] = display_df["Forecast"].apply(lambda x: f"₹{x/1e7:,.2f} Cr")
st.dataframe(display_df)

# ----------------------------
# PLOT FORECAST
# ----------------------------
fig2, ax2 = plt.subplots(figsize=(12, 4))
# Use store_df_inr for history and forecast_df_inr for forecast
ax2.plot(store_df_inr["Date"], store_df_inr["Weekly_Sales"], label="History")
ax2.plot(forecast_df_inr["Date"], forecast_df_inr["Forecast"], label="Forecast", marker="o")

ax2.set_title(f"Forecast Horizon: {horizon} Weeks — Store {selected_store} (in ₹ Rupees)")
ax2.set_ylabel("Weekly Sales (₹ Crores)")
ax2.legend()
# Format Y-axis to show Crores
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/1e7:,.2f} Cr'))
st.pyplot(fig2)

# ----------------------------
# DOWNLOAD BUTTON
# ----------------------------
csv = forecast_df_inr.to_csv(index=False).encode()
st.download_button("Download Forecast CSV (INR)", csv, "forecast_inr.csv")