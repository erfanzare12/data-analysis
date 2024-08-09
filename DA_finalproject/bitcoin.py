import streamlit as st
import pandas as pd
from plotly import graph_objects as go
from matplotlib import pyplot as plt


df = pd.read_csv(R"D:\python_src\DA_finalproject\result.csv")

st.title("Bitcoin(in the 5 last years)")

topic = st.selectbox("topic",["data frame", "describe", "candle stick", "plot of tolerance","correlation" , "analysis of benefit and tolerance"])

if topic=="analysis of benefit and tolerance":
    title = st.selectbox("title",["the most profitable weekday", "the most profitable month", "lowest tolerance weekday", "lowest tolerance month"])


if st.button("do it"):
    if topic=="data frame":
        st.write(df)

    elif topic=="describe":
        st.write(df.describe())
    
    elif topic=="candle stick":
        candle_stick = go.Figure(go.Candlestick(x=df.index, open=df.Open, high=df.High, low=df.Low, close=df.Close))
        
        st.plotly_chart(candle_stick)

    elif topic=="plot of tolerance":
        fig, ax = plt.subplots()
        ax.plot(df["Tolerance"])

        st.pyplot(fig)

    elif topic=="correlation":
        st.write("the table below shows the correlation between benefit and tolerance")
        st.write(df[["Benefit", "Tolerance"]].corr())



    elif title=="the most profitable weekday":
        st.write("the table below shows wich weekdays have the highest average benefit")
        st.write(df[["Benefit", "Weekday"]].groupby("Weekday").mean().sort_values(by="Benefit", ascending= False))
    
    elif title=="the most profitable month":
        st.write("the table below shows wich months have the highest average benefit")
        st.write(df[["Benefit", "Month"]].groupby("Month").mean().sort_values(by="Benefit", ascending= False))

    elif title=="lowest tolerance weekday":
        st.write("the table below shows wich weekdays have the lowest average telorance")
        st.write(df[["Tolerance", "Weekday"]].groupby("Weekday").mean().sort_values(by="Tolerance"))
    
    elif title=="lowest tolerance month":
        st.write("the table below shows wich months have the lowest average telorance")
        st.write(df[["Tolerance", "Month"]].groupby("Month").mean().sort_values(by="Tolerance"))
