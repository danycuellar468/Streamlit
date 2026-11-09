"""Build Plotly figures for Sales Explorer."""

import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure


def daily_units_chart(df: pd.DataFrame) -> Figure:
    """Return a line chart of total units sold per date."""
    daily = df.groupby("date", as_index=False, sort=True)["units"].sum()
    return px.line(daily, x="date", y="units", title="Daily units")


def top_skus_chart(df: pd.DataFrame) -> Figure:
    """Return a bar chart of the 10 SKUs with the highest total revenue."""
    top_skus = df.groupby("sku", as_index=False)["revenue"].sum().nlargest(10, "revenue")
    fig = px.bar(top_skus, x="sku", y="revenue", title="Top 10 SKUs by revenue")
    fig.update_xaxes(type="category")
    return fig