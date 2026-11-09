"""Load and clean the data for Sales Explorer."""

from pathlib import Path

import pandas as pd
import streamlit as st


def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize sales fields and remove rows missing essential values."""
    text_columns = ["sku", "category", "region"]
    numeric_columns = ["units", "revenue"]
    required_columns = ["date", *text_columns, *numeric_columns]

    sales = df.copy()
    sales.columns = sales.columns.str.strip().str.lower()
    missing = sorted(set(required_columns) - set(sales.columns))
    if missing:
        raise ValueError(f"Missing sales columns: {', '.join(missing)}")

    sales["date"] = pd.to_datetime(sales["date"], errors="coerce")
    for column in text_columns:
        sales[column] = sales[column].astype("string").str.strip().replace("", pd.NA)

    if "unit_price" in sales.columns:
        numeric_columns.append("unit_price")
    for column in numeric_columns:
        sales[column] = pd.to_numeric(sales[column], errors="coerce")

    return sales.dropna(subset=required_columns).reset_index(drop=True)


@st.cache_data
def load_sales(path: str | Path) -> pd.DataFrame:
    """Read a sales CSV and cache the cleaned DataFrame."""
    return clean_sales(pd.read_csv(path, dtype="string"))