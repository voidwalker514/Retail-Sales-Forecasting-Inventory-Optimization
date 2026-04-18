import pandas as pd


def preprocess_data(df):
    """
    Clean data and create features
    """

    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])

    # Time features
    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month
    df["weekday"] = df["date"].dt.weekday

    # Sort for lag features
    df = df.sort_values(["product", "date"])

    # Lag features (per product)
    df["lag_1"] = df.groupby("product")["sales"].shift(1)
    df["lag_7"] = df.groupby("product")["sales"].shift(7)

    df.dropna(inplace=True)

    return df