import numpy as np
import pandas as pd


def calculate_inventory_metrics(df, lead_time=7, z_score=1.65):
    """
    Calculate inventory metrics per product
    """

    results = []

    grouped = df.groupby("product")

    for product, data in grouped:
        avg_demand = data["forecast"].mean()
        std_demand = data["forecast"].std()

        safety_stock = z_score * std_demand * np.sqrt(lead_time)
        reorder_point = (avg_demand * lead_time) + safety_stock

        results.append({
            "Product": product,
            "Avg Demand": round(avg_demand, 2),
            "Std Dev": round(std_demand, 2),
            "Safety Stock": round(safety_stock, 2),
            "Reorder Point": round(reorder_point, 2)
        })

    return pd.DataFrame(results)