import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard ADRs", layout="wide")

st.title("📊 Variação dos ADRs Brasileiros (8h - 9h)")

tickers = ['PBR', 'VALE', 'BRFS', 'EBR', 'BBD', 'ITUB']

def get_variations():
    variations = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2d", interval="1h")
        try:
            df = hist.iloc[-2]
            open_price = df['Open']
            close_price = df['Close']
            variation = ((close_price - open_price) / open_price) * 100
            variations.append(round(variation, 2))
        except:
            variations.append(None)
    return variations

variations = get_variations()
df = pd.DataFrame({'Ticker': tickers, 'Variação (%)': variations})

fig = px.bar(df, x='Ticker', y='Variação (%)', color='Variação (%)',
             color_continuous_scale='RdBu', title='Variação entre 8h e 9h')

st.plotly_chart(fig, use_container_width=True)
