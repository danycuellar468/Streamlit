"""Connect the Sales Explorer interface to the data and chart modules."""

from pathlib import Path

import streamlit as st

from components.charts import daily_units_chart, top_skus_chart
from data.loaders import load_sales

DATA = Path(__file__).resolve().parents[2] / "data" / "sales_daily.csv"

st.set_page_config(page_title="Sales Explorer", layout="wide")
st.title("Sales Explorer")

df = load_sales(DATA)

with st.sidebar:
    regions = st.multiselect(
        "Region",
        sorted(df["region"].unique()),
        placeholder="All regions",
        key="sales_region_filter",
    )
    if regions:
        df = df[df["region"].isin(regions)]

    categories = st.multiselect(
        "Category",
        sorted(df["category"].unique()),
        placeholder="All categories",
        key="sales_category_filter",
    )
    if categories:
        df = df[df["category"].isin(categories)]
if df.empty:
    st.warning("No sales match the selected filters.")
    st.stop()

units_col, revenue_col, sku_col = st.columns(3)
units_col.metric("Total units", f"{df['units'].sum():,}")
revenue_col.metric("Total revenue", f"{df['revenue'].sum():,.2f}")
sku_col.metric("Unique SKUs", f"{df['sku'].nunique():,}")

st.plotly_chart(daily_units_chart(df), width="stretch")
st.plotly_chart(top_skus_chart(df), width="stretch")

with st.expander("Filtered sales rows"):
    st.dataframe(df, hide_index=True, width="stretch")