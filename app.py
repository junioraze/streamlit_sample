import yfinance as yf #finance data from yahoo api
import streamlit as st #streamlit for building a data-driven web app
import pandas as pd #pandas for manipulate data

# st.write can read markdown style and pass the string to the web app
st.write("""
## Simple streamlit app

* Show the stock closing price and volume of Google.

""")

#hardcoding the google stock ticker
ticker_symbol = 'GOOGL'

#get the ticker data
ticker_data = yf.Ticker(ticker_symbol)

#create a datafram between the dates by the period
ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2020-5-31')

#create the two line charts of Close and Volume
st.line_chart(ticker_df['Close'])
st.line_chart(ticker_df['Volume'])