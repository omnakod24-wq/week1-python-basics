"""Week 4: analyze sales data and create charts plus a Markdown report."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
DATA = BASE / "data" / "sales_data.csv"
CHARTS = BASE / "visualizations"
REPORT = BASE / "report"
REQUIRED = {"Date", "Product", "Quantity", "Price", "Customer_ID", "Region", "Total_Sales"}


def load_data(path=DATA):
    """Load CSV and validate required columns."""
    df = pd.read_csv(path)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError("Missing required columns: " + ", ".join(sorted(missing)))
    return df


def clean_data(df):
    """Convert types, remove duplicates and exclude invalid essential values."""
    result = df.copy()
    result["Date"] = pd.to_datetime(result["Date"], errors="coerce")
    for col in ["Quantity", "Price", "Total_Sales"]:
        result[col] = pd.to_numeric(result[col], errors="coerce")
    for col in ["Product", "Customer_ID", "Region"]:
        result[col] = result[col].astype("string").str.strip()
    result = result.drop_duplicates().dropna(subset=["Date", "Product", "Quantity", "Price"])
    result = result[(result["Product"] != "") & (result["Quantity"] >= 0) & (result["Price"] >= 0)]
    result["Total_Sales"] = result["Quantity"] * result["Price"]
    result["Region"] = result["Region"].fillna("Unknown").replace("", "Unknown")
    result["Customer_ID"] = result["Customer_ID"].fillna("Unknown").replace("", "Unknown")
    return result.sort_values("Date").reset_index(drop=True)


def create_charts(df):
    """Create a bar chart, line chart and pie chart."""
    CHARTS.mkdir(parents=True, exist_ok=True)
    REPORT.mkdir(parents=True, exist_ok=True)
    products = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
    plt.figure(figsize=(9, 5))
    products.plot(kind="bar")
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales (INR)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS / "sales_by_product.png", dpi=150)
    plt.close()

    monthly = df.set_index("Date").resample("MS")["Total_Sales"].sum()
    plt.figure(figsize=(9, 5))
    monthly.plot(kind="line", marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales (INR)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CHARTS / "monthly_sales_trend.png", dpi=150)
    plt.close()

    regions = df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
    plt.figure(figsize=(7, 7))
    regions.plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title("Sales Share by Region")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(CHARTS / "sales_by_region.png", dpi=150)
    plt.close()
    return products, monthly, regions


def write_report(original, df, products, monthly, regions):
    """Write findings and links to generated charts."""
    if df.empty:
        content = "# Sales Analysis Report\n\nNo valid records remained after cleaning.\n"
    else:
        best_product, best_month, best_region = products.idxmax(), monthly.idxmax(), regions.idxmax()
        content = f"""# Sales Data Analysis Report

## Project overview
This project analyzes the supplied practice sales dataset using Python, pandas, and Matplotlib.

## Data quality
- Original rows: {len(original)}
- Rows after cleaning: {len(df)}
- Duplicate rows removed: {len(original) - len(original.drop_duplicates())}
- Missing values remaining: {int(df.isna().sum().sum())}
- Date range: {df['Date'].min().date()} to {df['Date'].max().date()}

## Key metrics
- **Total revenue:** ₹{df['Total_Sales'].sum():,.2f}
- **Average sale:** ₹{df['Total_Sales'].mean():,.2f}
- **Highest individual sale:** ₹{df['Total_Sales'].max():,.2f}
- **Lowest individual sale:** ₹{df['Total_Sales'].min():,.2f}
- **Units sold:** {df['Quantity'].sum():,.0f}
- **Unique customers:** {df['Customer_ID'].nunique()}

## Findings
- **Top product by revenue:** {best_product} (₹{products[best_product]:,.2f}).
- **Highest-revenue month:** {best_month.strftime('%B %Y')} (₹{monthly[best_month]:,.2f}).
- **Highest-revenue region:** {best_region} (₹{regions[best_region]:,.2f}).

## Visualizations
### Sales by product
![Sales by product](../visualizations/sales_by_product.png)

### Monthly sales trend
![Monthly trend](../visualizations/monthly_sales_trend.png)

### Sales share by region
![Sales by region](../visualizations/sales_by_region.png)

## Method
1. Load the CSV with pandas.
2. Validate columns and convert dates and numbers.
3. Remove exact duplicates and records missing essential fields.
4. Recalculate revenue as Quantity multiplied by Price.
5. Group sales by product, month, and region.
6. Generate three charts and save this report.

## Setup
Install dependencies with py -m pip install -r requirements.txt on Windows, then run py main.py. On macOS/Linux use python3 -m pip install -r requirements.txt and python3 main.py.

## Limitations
This is a practice dataset, not verified real-world business data. Findings describe only the supplied records.
"""
    REPORT.mkdir(parents=True, exist_ok=True)
    (REPORT / "analysis_report.md").write_text(content, encoding="utf-8")
    return content


def main():
    """Run the complete data analysis workflow."""
    try:
        original = load_data()
        df = clean_data(original)
        if df.empty:
            raise ValueError("No valid records remain after cleaning.")
        products, monthly, regions = create_charts(df)
        write_report(original, df, products, monthly, regions)
        print("WEEK 4 - COMPLETE SALES DATA ANALYSIS")
        print("=" * 40)
        print(f"Original rows: {len(original)}")
        print(f"Rows after cleaning: {len(df)}")
        print(f"Total revenue: ₹{df['Total_Sales'].sum():,.2f}")
        print(f"Average sale: ₹{df['Total_Sales'].mean():,.2f}")
        print(f"Top product: {products.idxmax()}")
        print(f"Top region: {regions.idxmax()}")
        print("Charts saved in visualizations/")
        print("Report saved in report/analysis_report.md")
    except FileNotFoundError:
        print(f"Error: dataset not found at {DATA}. Check data/sales_data.csv.")
    except (ValueError, pd.errors.ParserError) as exc:
        print(f"Data error: {exc}")


if __name__ == "__main__":
    main()
