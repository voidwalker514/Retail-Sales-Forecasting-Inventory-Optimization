from sklearn.ensemble import RandomForestRegressor


FEATURES = ["day", "month", "weekday", "lag_1", "lag_7"]


def train_forecasting_model(df):
    """
    Train Random Forest model
    """

    X = df[FEATURES]
    y = df["sales"]

    model = RandomForestRegressor(
        n_estimators=150,
        max_depth=6,
        random_state=42
    )

    model.fit(X, y)

    return model


def make_predictions(model, df):
    """
    Generate predictions
    """

    df = df.copy()
    df["forecast"] = model.predict(df[FEATURES])

    return df
