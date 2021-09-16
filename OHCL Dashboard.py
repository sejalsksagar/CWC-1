import json_to_csv as jc
import plot_graph as gg
import streamlit as st
import reader as rr
import pandas as pd


jc.convert_to_csv()
st.title("OPEN-HIGH-LOW-CLOSE CHARTS")
st.write("Open-high-low-close chart (OHLC) is a type of chart typically used to illustrate \
movements in the price of a financial instrument over time.")

symbol = st.text_input("Enter Company Symbol: ")
if len(symbol) != 0:
    #write entered symbol in input.txt
    symbol = symbol.upper()
    file = open("input.txt", "a")
    file.write(symbol + "\n")
    file.close()

    #find symbol in StockList_csv.csv
    count = rr.find_symbol(symbol)
    if(count == 0):
        st.write("SYMBOL NOT FOUND")
    else:
        original_list = ['OHLC', 'Colored Bar', 'Vertex Line']
        result = st.selectbox('Select graph type: ', original_list)
        fn = "Symbols.csv"

        if len(result) != 0:
            if(result == "OHLC"):
                fig = gg.ohlc(fn)
                st.plotly_chart(fig)

            elif(result == "Colored Bar"):
                fig = gg.colored_bar(fn)
                st.plotly_chart(fig)

            elif(result == "Vertex Line"):
                fig = gg.vertex_line(fn)
                st.plotly_chart(fig)


st.sidebar.title("What is OHLC?")
st.sidebar.write("- An OHLC chart shows the open, high, low, and close price for a given period.")
st.sidebar.write("- It can be applied to any timeframe.")
st.sidebar.write("- The vertical line represents the high and low for the period, while the line to the left \
marks the open price and the line to the right marks the closing price. This entire \
structure is called a bar.")
st.sidebar.write("- When the close is above the open, the bar is often colored black. When the close is \
below the open the bar is often colored red.")