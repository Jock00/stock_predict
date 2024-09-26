from flask import Flask, request, jsonify
import logging
from stock_price_prediction import StockPricePredictor

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/predict', methods=['POST'])
def predict_stock_prices():
    """API endpoint to predict stock prices."""
    data = request.json
    securities_directory = data.get('exchange')
    num_securities = data.get('num_securities', 1)

    try:
        predictor = StockPricePredictor(securities_directory)
        predicted_values = predictor.predict(num_securities)
        return jsonify(predicted_values)
    except Exception as e:
        logging.error(f"Error in prediction: {e}")
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
