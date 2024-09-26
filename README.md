# Stock Price Predictor

A Flask-based application for predicting stock prices using linear regression. This project loads historical stock data from CSV files, trains a prediction model, and provides predictions for future stock prices.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)

## Features
- Load historical stock data from CSV files.
- Randomly select entries for prediction.
- Train a linear regression model on historical data.
- Predict future stock prices based on the trained model.
- Save prediction results to CSV files.

## Installation
To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Jock00/stock_predict.git
   cd stock-price-predictor
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place your stock data CSV files in the `stock_price_data_files` directory.
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Use the API to make predictions.

## API Endpoints
### `POST /predict`
Predicts stock prices for a given exchange.

**Request Body:**
```json
{
    "exchange": "your_exchange_type",
    "num_securities": 3
}
```

- `exchange`: The directory containing stock data CSV files.
- `num_securities`: The number of files.

**Example Request:**
```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"exchange": "NYSE", "num_securities": 2}'
```
**Response:**
Returns a JSON array of predicted stock prices (which will be saved in 
`prediction_results`.
```json
[
    {
        "security": "stock_1.csv",
        "predicted_values": [123.45, 125.67, 128.90]
    },
    ...
]
```

## Directory Structure
```
/stock-price-predictor
├── app.py                        # Main application file
├── stock_price_data_files        # Directory for stock data CSV files
├── prediction_results             # Directory for saving prediction results
├── requirements.txt               # Required Python packages
└── README.md                     # Project documentation
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

