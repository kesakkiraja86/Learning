import streamlit as st
import plotly.express as px
from utils import get_data

st.title("Sales Dashboard")

df = get_data()

st.dataframe(df)

fig = px.bar(
    df,
    x="product",
    y="sales",
    title="Sales by Product"
)

st.plotly_chart(fig)
