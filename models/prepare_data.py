import pandas as pd
import numpy as np

def prepare_data():
    column_order = ['Date', 'Bid', 'Ask', 'Opening price', 'High price', 'Low price', 'Closing price', 'Average price', 'Total volume', 'Turnover', 'Trades']
    data = pd.read_csv("../data/SHB_A-1999-01-06-2024-02-05.csv", sep=";", decimal=",", skiprows=1, usecols=column_order)
    
    data = data.iloc[::-1]
    data.dropna()

    data["Diff"] = data["Closing price"].diff()

    FACTOR = 0.0135 # Profit to define target 0.014

    SHORT_CHANGE_HORIZON = 5
    MID_CHANGE_HORIZON = 20
    LONG_CHANGE_HORIZON = 50
    FACTOR = 0.014 # Profit to define target 0.0135
    # FACTOR = 0

    data["Short_day_change"] = (data["Closing price"] - data["Closing price"].shift(SHORT_CHANGE_HORIZON)) / SHORT_CHANGE_HORIZON
    data["Mid_day_change"] = (data["Closing price"] - data["Closing price"].shift(MID_CHANGE_HORIZON)) / MID_CHANGE_HORIZON
    data["Long_day_change"] = (data["Closing price"] - data["Closing price"].shift(LONG_CHANGE_HORIZON)) / LONG_CHANGE_HORIZON


    data["t+1"] = data["Closing price"].shift(-1)
    data["t+2"] = data["Closing price"].shift(-2)
    data["t+4"] = data["Closing price"].shift(-4)
    data["t+5"] = data["Closing price"].shift(-5)
    data["t+3"] = data["Closing price"].shift(-3)

    conditions = [
        (data["t+1"] > (data["Closing price"] * (1+FACTOR))) |
        (data["t+2"] > (data["Closing price"] * (1+FACTOR))) |
        (data["t+3"] > (data["Closing price"] * (1+FACTOR))) |
        (data["t+4"] > (data["Closing price"] * (1+FACTOR))) |
        (data["t+5"] > (data["Closing price"] * (1+FACTOR)))
    ]


    choice = [1]
    data["Target"] = np.select(conditions, choice, 0)

    data = data.dropna()

    return data