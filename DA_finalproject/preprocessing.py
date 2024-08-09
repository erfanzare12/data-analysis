import numpy as np
import pandas as pd


df = pd.read_csv("BTC-USD.csv")

df = df.drop(columns=["Adj Close", "Volume"])
df["Date"] = pd.to_datetime(df["Date"])

df["Benefit"] = df["Close"] - df["Open"]
df["Tolerance"] = df["High"] - df["Low"]
df["Month"] = df["Date"].apply(lambda d: d.month).astype(np.uint8)
df["Weekday"] = df["Date"].apply(lambda d: d.isoweekday()).astype(np.uint8)

df.to_csv("result.csv", index=False)