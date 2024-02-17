import pandas as pd
import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import metrics
import csv

def avg_ownership_period():
    user_data = pd.read_csv('src/user_stat.csv')
    return {"AVG:":user_data[user_data['OwnershipPeriod'].notnull()].mean(),"MAX":user_data[user_data['OwnershipPeriod'].notnull()].max(),"MIN":user_data[user_data['OwnershipPeriod'].notnull()].min()}

def retreive_user_data():
    pass

def Get_stock_history():
    data = []
    with open('src/user_stat.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data[1:]


def Predict_best_dates(days):
    df = yf.download(tickers= 'BTC-USD',start='2023-10-01', end='2024-02-11')
    df["Date"] = df.index
    df = df[["Date", "Open", "High","Low", "Close", "Volume"]]
    df.reset_index(drop=True, inplace=True)
    df['stamp'] = [i for i in range(1,df.shape[0]+1)]
    X = df[['stamp']]
    Y = df['Close']
    x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0)   # splitting the data
    linReg= LinearRegression()
    linReg.fit(x_train, y_train)    # training the model
    linReg_prediction=linReg.predict(x_test) # predicting the close prices
    df['Avg'] = (df['Open']+df['Close'])/2
    close_prices = np.array(df['Avg'])  # Close prices
    open_prices = np.array(df['stamp'])  # Open prices
    slope, intercept = np.polyfit(open_prices, close_prices, 1)    # finding the slope and intercept
    RMSE = np.sqrt(metrics.mean_squared_error(y_test,linReg_prediction)) # root mean square error
    return slope * days  + intercept - RMSE




