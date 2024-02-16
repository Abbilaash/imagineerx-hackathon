'''import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt'''
import yfinance as yf
symbol='BTC-USD'
ticker = yf.Ticker(symbol)
real_time_data=ticker.history(period='1s')
while True:
    print(real_time_data)
def hehe():
    df = pd.read_csv('your_dataset.csv')
    target_column = 'Close'
    features = ['Open']
    X = df[features].values.reshape(-1, 1)
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    plt.scatter(X_test, y_test, color='black', label='Actual Prices')
    plt.plot(X_test, predictions, color='blue', linewidth=3, label='Predicted Prices')
    plt.xlabel('Open Price')
    plt.ylabel('Close Price')
    plt.title('Cryptocurrency Price Prediction')
    plt.legend()
    plt.show()
