import streamlit as st
import plotly.express as px

from utils import get_data

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("Sales Dashboard")
st.caption("Product sales from demo_cat.demo_schema.sales_demo")

df = get_data()

# --- KPI metrics ---------------------------------------------------------
total_sales = df["sales"].sum()
top_product = df.loc[df["sales"].idxmax()]

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Products", len(df))
col3.metric("Top Product", f"{top_product['product']} (${top_product['sales']:,.0f})")

# --- Chart ---------------------------------------------------------------
fig = px.bar(
    df,
    x="product",
    y="sales",
    title="Sales by Product",
)
fig.update_traces(texttemplate="%{y:,.0f}", textposition="outside")
fig.update_yaxes(title="Sales ($)")

st.plotly_chart(fig, width="stretch")

# --- Data table ------------------------------------------------------------
st.subheader("Data")
st.dataframe(df, width="stretch", hide_index=True)
