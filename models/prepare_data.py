import pandas as pd
import numpy as np

def prepare_data(short_day, mid_day, long_day, change_factor):
    column_order = ['Date', 'Bid', 'Ask', 'Opening price', 'High price', 'Low price', 'Closing price', 'Average price', 'Total volume', 'Turnover', 'Trades']
    data = pd.read_csv("../data/SHB_A-1999-01-06-2024-02-05.csv", sep=";", decimal=",", skiprows=1, usecols=column_order)
    
    data = data.iloc[::-1]
    data.dropna()

    data["Diff"] = data["Closing price"].diff()

    # change_factor = 0.0135 # Profit to define target 0.014

    # short_day = 5
    # mid_day = 20
    # long_day = 50
    # change_factor = 0.014 # Profit to define target 0.0135
    # change_factor = 0

    data["Short_day_change"] = (data["Closing price"] - data["Closing price"].shift(short_day)) / short_day
    data["Mid_day_change"] = (data["Closing price"] - data["Closing price"].shift(mid_day)) / mid_day
    data["Long_day_change"] = (data["Closing price"] - data["Closing price"].shift(long_day)) / long_day


    data["t+1"] = data["Closing price"].shift(-1)
    data["t+2"] = data["Closing price"].shift(-2)
    data["t+4"] = data["Closing price"].shift(-4)
    data["t+5"] = data["Closing price"].shift(-5)
    data["t+3"] = data["Closing price"].shift(-3)

    conditions = [
        (data["t+1"] > (data["Closing price"] * (1+change_factor))) |
        (data["t+2"] > (data["Closing price"] * (1+change_factor))) |
        (data["t+3"] > (data["Closing price"] * (1+change_factor))) |
        (data["t+4"] > (data["Closing price"] * (1+change_factor))) |
        (data["t+5"] > (data["Closing price"] * (1+change_factor)))
    ]


    choice = [1]
    data["Target"] = np.select(conditions, choice, 0)

    data = data.dropna()

    return data