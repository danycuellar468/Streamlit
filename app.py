"""Activity 1 starter: a deliberately notebook-style Streamlit app.

Goal (30 min): run it, finish the TODOs, push it to GitHub and deploy it
on Streamlit Community Cloud. Everything is in ONE file on purpose:
Activity 2 refactors it into modules.

Run from the kit root:   streamlit run session1/activity1_starter/app.py

When you move this app to YOUR OWN repo: copy data/sales_daily.csv next to
app.py and change DATA to Path(__file__).parent / "sales_daily.csv".
"""
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATA = Path(__file__).parent / "sales_daily.csv"

st.set_page_config(page_title="Sales Explorer", layout="wide")
st.title("Sales Explorer")

df = pd.read_csv(DATA, parse_dates=["date"])

# TODO 1: add a region filter (st.selectbox or st.multiselect) and filter df
regions = st.multiselect("Region", sorted(df["region"].unique()), placeholder="All regions")
if regions:
    df = df[df["region"].isin(regions)]

# TODO 2: add a category filter the same way
categories = st.multiselect(
    "Category", sorted(df["category"].unique()), placeholder="All categories"
)
if categories:
    df = df[df["category"].isin(categories)]

daily = df.groupby("date", as_index=False)["units"].sum()
fig = px.line(daily, x="date", y="units", title="Daily units")
st.plotly_chart(fig, width="stretch")

# TODO 3: add KPI cards with st.columns + st.metric (total units, revenue, # SKUs)
units_col, revenue_col, sku_col = st.columns(3)
units_col.metric("Total units", f"{df['units'].sum():,}")
revenue_col.metric("Total revenue", f"{df['revenue'].sum():,.2f}")
sku_col.metric("Unique SKUs", f"{df['sku'].nunique():,}")

# TODO 4: add a second chart: top 10 SKUs by revenue (px.bar)
top_skus = df.groupby("sku", as_index=False)["revenue"].sum().nlargest(10, "revenue")
fig_skus = px.bar(top_skus, x="sku", y="revenue", title="Top 10 SKUs by revenue")
st.plotly_chart(fig_skus, width="stretch")

# TODO 5 (stretch): show the filtered rows in st.dataframe inside an st.expander
with st.expander("Filtered sales rows"):
    st.dataframe(df, hide_index=True, width="stretch")