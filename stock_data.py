import pandas as pd
import numpy as np

class StockData:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """Load stock data from CSV file."""
        try:
            data = pd.read_csv(self.file_path, header=None,
                               names=['Security Type', 'Timestamp',
                                      'Stock Price'])
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{self.file_path}' not found.")
        except pd.errors.EmptyDataError:
            raise ValueError(f"File '{self.file_path}' is empty.")
        except pd.errors.ParserError:
            raise ValueError(f"Error parsing the file '{self.file_path}'.")
        except Exception as e:
            raise RuntimeError(f"Error reading file '{self.file_path}': {e}")

    def get_random_historical_data(self) -> pd.DataFrame:
        """Retrieve random historical data for prediction."""
        if self.data is None or self.data.empty:
            raise ValueError("Security data not loaded or is empty.")

        random_index = np.random.randint(0, len(self.data) - 10)
        return self.data.iloc[random_index:random_index + 10]