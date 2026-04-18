"""
Multi-Product Retail Forecasting Dashboard
"""
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd

from src.data_generator import generate_sales_data
from src.preprocessing import preprocess_data
from src.forecasting import train_forecasting_model, make_predictions
from src.inventory import calculate_inventory_metrics

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Retail Forecasting Dashboard",
    layout="wide"
)

st.title("🛒 Retail Sales Forecasting & Inventory Optimization")

st.markdown("Simulate demand, forecast sales, and optimize inventory for multiple products.")

# ===============================
# SIDEBAR SETTINGS
# ===============================
st.sidebar.header("⚙️ Simulation Settings")

days = st.sidebar.slider("Number of Days", 100, 1000, 365)
num_products = st.sidebar.slider("Number of Products", 2, 20, 5)
lead_time = st.sidebar.slider("Lead Time (Days)", 1, 30, 7)
z_score = st.sidebar.slider("Service Level (Z-Score)", 1.0, 2.5, 1.65)

run_button = st.sidebar.button("🚀 Run Simulation")

# ===============================
# MAIN LOGIC
# ===============================
if run_button:

    # ---------------------------
    # DATA GENERATION
    # ---------------------------
    st.subheader("📊 Generated Sales Data")
    df = generate_sales_data(days, num_products)
    st.dataframe(df.head())

    # ---------------------------
    # PREPROCESSING
    # ---------------------------
    df_processed = preprocess_data(df)

    # ---------------------------
    # MODEL TRAINING
    # ---------------------------
    with st.spinner("Training model..."):
        model = train_forecasting_model(df_processed)

    # ---------------------------
    # PREDICTIONS
    # ---------------------------
    df_forecast = make_predictions(model, df_processed)

    # ---------------------------
    # PRODUCT SELECTION
    # ---------------------------
    st.subheader("📈 Product-wise Forecast")

    products = df_forecast["product"].unique()
    selected_product = st.selectbox("Select Product", products)

    df_product = df_forecast[df_forecast["product"] == selected_product]

    # ---------------------------
    # CHART
    # ---------------------------
    st.line_chart(
        df_product.set_index("date")[["sales", "forecast"]]
    )

    # ---------------------------
    # INVENTORY CALCULATION
    # ---------------------------
    st.subheader("📦 Inventory Optimization (All Products)")

    inventory_df = calculate_inventory_metrics(
        df_forecast,
        lead_time=lead_time,
        z_score=z_score
    )

    st.dataframe(inventory_df)

    # ---------------------------
    # HIGHLIGHT INSIGHTS
    # ---------------------------
    st.subheader("🔍 Key Insights")

    high_risk = inventory_df.sort_values("Reorder Point", ascending=False).head(1)
    low_demand = inventory_df.sort_values("Avg Demand").head(1)

    col1, col2 = st.columns(2)

    with col1:
        st.warning(f"⚠️ Highest Reorder Need: {high_risk['Product'].values[0]}")

    with col2:
        st.info(f"📉 Lowest Demand Product: {low_demand['Product'].values[0]}")

    # ---------------------------
    # DOWNLOAD BUTTONS
    # ---------------------------
    st.subheader("📥 Download Results")

    st.download_button(
        label="Download Forecast Data",
        data=df_forecast.to_csv(index=False),
        file_name="forecast_data.csv",
        mime="text/csv"
    )

    st.download_button(
        label="Download Inventory Report",
        data=inventory_df.to_csv(index=False),
        file_name="inventory_report.csv",
        mime="text/csv"
    )

else:
    st.info("👉 Use the sidebar and click 'Run Simulation' to start.")