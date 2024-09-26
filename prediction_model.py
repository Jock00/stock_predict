import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
class PredictionModel:
    def __init__(self, historical_data: pd.DataFrame):
        self.historical_data = historical_data
        self.model = LinearRegression()

    def train(self) -> None:
        """Train the linear regression model."""
        X = self.historical_data.index.values.reshape(-1, 1)
        y = self.historical_data['Stock Price'].values
        self.model.fit(X, y)

    def predict(self, future_timestamps: np.ndarray) -> np.ndarray:
        """Predict future stock prices."""
        return self.model.predict(future_timestamps.reshape(-1, 1))