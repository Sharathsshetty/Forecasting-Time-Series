#import libarires
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import datetime
from datetime import date, timedelta
#from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller



#Title
app_name='Stock Market Forecasting on Tata Motors'
st.title(app_name)
st.subheader('Stock Data')

#add an amgefrom online resource


#take input from the user of app about the start and end date

#sidebar
st.sidebar.header('Selcet the parameters from below')


start_date = st.sidebar.date_input("Start date", date(2003, 1, 1))
end_date = st.sidebar.date_input("End date", date(2023, 12, 31))

#add ticker symbol list

ticker_list = ["TATAMOTORS.NS"]
ticker=st.sidebar.selectbox('Select the compay', ticker_list)

data=yf.download(ticker, start=start_date, end=end_date)

data.insert(0,"Date", data.index,True)
data.reset_index(drop=True, inplace=True)
st.write('Data from', start_date, 'to', end_date)
st.write(data)


#plot the data
st.header('Data Visualization')
st.subheader('Plost of the data')
fig=px.line(data, x='Date', y=data.columns, title='Closing price of the stock', width=1000, height=600)
st.plotly_chart(fig)


column=st.selectbox('Select the column to be use for forecasting', data.columns[1:] )



#subsetting the data

data=data[['Date', column]]
st.write("Selected Data")
st.write(data)

#ADF test check stationary
st.header('Is data stationary')
#st.write('**Note:** If p-value is less than 0.05, then data is stationary')
st.write(adfuller(data[column])[1])
