"""
Retail Sales Forecasting & Inventory Optimization
Multi-Product Version
"""

import os

from src.data_generator import generate_sales_data
from src.preprocessing import preprocess_data
from src.forecasting import train_forecasting_model, make_predictions
from src.inventory import calculate_inventory_metrics


def main():
    print("\n🚀 Starting Retail Forecasting Pipeline...\n")

    # ==============================
    # CREATE REQUIRED FOLDERS
    # ==============================
    os.makedirs("data", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    try:
        # ==============================
        # STEP 1: GENERATE DATA
        # ==============================
        print("📊 Generating synthetic data...")
        df = generate_sales_data(days=365, num_products=5)

        df.to_csv("data/sales_data.csv", index=False)

        # ==============================
        # STEP 2: PREPROCESS
        # ==============================
        print("🧹 Preprocessing data...")
        df = preprocess_data(df)

        # ==============================
        # STEP 3: TRAIN MODEL
        # ==============================
        print("🤖 Training forecasting model...")
        model = train_forecasting_model(df)

        # ==============================
        # STEP 4: PREDICTIONS
        # ==============================
        print("📈 Generating predictions...")
        df = make_predictions(model, df)

        df.to_csv("outputs/forecast_results.csv", index=False)

        # ==============================
        # STEP 5: INVENTORY OPTIMIZATION
        # ==============================
        print("📦 Calculating inventory metrics...")
        inventory_df = calculate_inventory_metrics(df)

        inventory_df.to_csv("outputs/inventory_report.csv", index=False)

        # ==============================
        # FINAL OUTPUT
        # ==============================
        print("\n📊 INVENTORY REPORT:")
        print(inventory_df)

        print("\n✅ Project executed successfully!")

    except Exception as e:
        print(f"\n❌ Error occurred: {e}")


# ==============================
# ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()