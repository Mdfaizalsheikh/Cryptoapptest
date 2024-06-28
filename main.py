import streamlit as st
import requests
import pandas as pd
import time
from dotenv import load_dotenv
import os


load_dotenv()

st.title("Cryptocurrency Price Tracker")


cryptos = ["Bitcoin", "Ethereum", "Ripple", "Litecoin", "Bitcoin Cash"]


crypto_symbols = {
    "Bitcoin": "BTC",
    "Ethereum": "ETH",
    "Ripple": "XRP",
    "Litecoin": "LTC",
    "Bitcoin Cash": "BCH"
}


selected_crypto = st.selectbox("Select a Cryptocurrency", cryptos)
symbol = crypto_symbols[selected_crypto]


def get_crypto_price(symbol):
    api_url = os.getenv("API_URL").replace("{symbol}", symbol)
    response = requests.get(api_url)
    data = response.json()
    price = data[symbol.lower()]["usd"]
    return price


st.subheader(f"Real-Time {selected_crypto} Price")

price_chart = st.line_chart()

while True:
    price = get_crypto_price(symbol)
    current_time = time.strftime("%H:%M:%S")
    new_row = pd.DataFrame([[current_time, price]], columns=["Time", "Price"])
    price_chart.add_rows(new_row)
    st.write(f"Current {selected_crypto} Price: ${price}")
    time.sleep(5)
streamlit runru
