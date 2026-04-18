import pandas as pd
import numpy as np


def generate_sales_data(days=365, num_products=5):
    """
    Generate synthetic multi-product retail sales data
    """

    np.random.seed(42)

    dates = pd.date_range(start="2024-01-01", periods=days)
    products = [f"Product_{i+1}" for i in range(num_products)]

    data = []

    for product in products:
        base_sales = np.random.randint(20, 100)

        seasonality = 10 * np.sin(np.linspace(0, 3 * np.pi, days))
        noise = np.random.normal(0, 5, days)

        sales = base_sales + seasonality + noise

        for i in range(days):
            data.append([
                dates[i],
                product,
                int(max(sales[i], 0))
            ])

    df = pd.DataFrame(data, columns=["date", "product", "sales"])

    return df