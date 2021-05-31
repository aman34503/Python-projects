import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
from datetime import date, timedelta
today = date.today()

d1 = today.strftime("%Y/%m/%d")
end_date = d1
d2 = date.today() - timedelta(days=360)
d2 = d2.strftime("%Y/%m/%d")
start_date = d2
import streamlit as st
st.title("Real-time Stock Price Data")
a = st.text_input("Enter Any Company >>:")
data = web.DataReader(name=a, data_source='yahoo', start=start_date, end=end_date)
fig, ax = plt.subplots()
ax = data["Close"].plot(figsize=(12, 8), title=a+" Stock Prices", fontsize=20, label="Close Price")
plt.legend()
plt.grid()
st.pyplot(fig)



# To run your file just execute the streamlit run filename.py in your terminal. In the output, you will get to see a user interface

# Just write the name of any company in the user input. Make sure that you write the shortcut of the name of the company listed in the stock exchange. Below is how you will see your final result after clicking enter.

# To create a realtime stock price data visualization application, I will be using the streamlit library in Python. In this task, we can use the streamlit library to create an interactive user interface where a user will enter the name of any company and the stock price data will be visualized as the final output.

# For the task of visualizing stock prices, we can use any data visualization library in Python compatible with the streamlit framework. But to keep it simple, I’ll be using the matplotlib library in Python.