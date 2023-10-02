# Stock Price Prediction AI Project

This AI project utilizes Long Short-Term Memory (LSTM) models for time series forecasting to predict stock prices. It includes various components and files to facilitate the prediction process.

## Project Components

### ML Model
- File: `ML_Model_for_ADAMS_Stock.py`
- Description: This file contains the Python code for training and implementing the LSTM model for stock price prediction.

### Saved Model
- File: `ADAMS_1.4.h5`
- Description: The trained LSTM model is saved in this file for later use in making predictions.

### Dataset
- File: `Adam Sugar Mills Limited.csv`
- Description: The dataset used for training and testing the model, containing historical stock price data.

### Data Scraper
- File: `data_scraper.py`
- Description: A Python script used to scrape and collect stock price data from stock exchange.

### Database
- File: `stock.db`
- Description: This SQLite database stores historical stock price data, stores new data fetched by 'data_scrapper.py' and the predictions made by model for easy retrieval and analysis.

### Get Predictions
- File: `get_predictions.py`
- Description: A Python script to obtain stock price predictions using the trained LSTM model.

### APP
- File: `pred_stocks_app.py`
- Description: The main application file, responsible for providing a user interface to interact with the model and view predictions.

## Usage

1. Ensure you have all the required files and dependencies installed.
2. Run main to fetch data from database and make predictions.
3. Use the `pred_stocks_app.py` to visualize predictions in GUI.


