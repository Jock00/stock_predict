import os
from stock_data import StockData
import numpy as np
from prediction_model import PredictionModel
import logging
import pandas as pd
logging.basicConfig(level=logging.INFO)


class StockPricePredictor:
    def __init__(self, securities_directory: str):
        self.securities_directory = os.path.join("stock_price_data_files",
                                                 securities_directory)

    def get_security_files(self) -> list:
        """Get a list of CSV files in the directory."""
        return [os.path.join(self.securities_directory, f)
                for f in os.listdir(self.securities_directory)
                if f.endswith('.csv')]

    def predict(self, num_securities: int) -> list:
        """Predict stock prices for a random selection of securities."""
        security_files = np.random.choice(
            self.get_security_files(), num_securities, replace=False)
        predictions = []

        # Ensure the prediction_results directory exists
        os.makedirs("prediction_results", exist_ok=True)

        for security_file in security_files:
            logging.info(f"Processing file: {security_file}")
            try:
                security_data = StockData(security_file)
                historical_data = security_data.get_random_historical_data()
                prediction_model = PredictionModel(historical_data)
                prediction_model.train()

                future_timestamps = np.array(
                    [historical_data.index[-1] + i for i in range(1, 4)])
                predicted_values = prediction_model.predict(future_timestamps)
                predictions.append({
                    'security': os.path.basename(security_file),
                    'predicted_values': predicted_values.tolist()
                })

                # Save predictions to a CSV file
                output_file = os.path.join("prediction_results",
                           f"{os.path.splitext(os.path.basename(
                               security_file))[0]}_predictions.csv")
                pd.DataFrame({'Stock-ID': [os.path.basename(security_file)] * 3,
                              'Timestamp': future_timestamps,
                              'Stock Price': predicted_values}).to_csv(
                    output_file, index=False)

            except Exception as e:
                logging.error(
                    f"Error processing security file '{security_file}': {e}")

        return predictions
