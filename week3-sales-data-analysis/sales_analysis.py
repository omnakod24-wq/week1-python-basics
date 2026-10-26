"""Week 3 project: Sales Data Analysis using pandas."""
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "sales_data.csv"
REPORT_FILE = BASE_DIR / "analysis_report.md"
REQUIRED_COLUMNS = {"Product", "Quantity", "Unit_Price", "Total_Sales", "Region"}


def load_data(path=DATA_FILE):
    """Load CSV data and check required columns."""
    df = pd.read_csv(path)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"CSV is missing required columns: {', '.join(sorted(missing))}")
    return df


def clean_data(df):
    """Clean missing, invalid and duplicate sales records."""
    cleaned = df.copy()
    cleaned["Product"] = cleaned["Product"].astype("string").str.strip()
    cleaned["Region"] = cleaned["Region"].astype("string").str.strip()
    for column in ["Quantity", "Unit_Price", "Total_Sales"]:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")
    cleaned = cleaned.drop_duplicates()
    cleaned = cleaned.dropna(subset=["Product", "Quantity", "Unit_Price"])
    cleaned = cleaned[(cleaned["Product"] != "") & (cleaned["Quantity"] >= 0) & (cleaned["Unit_Price"] >= 0)]
    # Recalculate sales so missing or incorrect values do not affect the analysis.
    cleaned["Total_Sales"] = cleaned["Quantity"] * cleaned["Unit_Price"]
    cleaned["Region"] = cleaned["Region"].fillna("Unknown").replace("", "Unknown")
    return cleaned


def build_report(original, df):
    """Return a Markdown report with key metrics and findings."""
    if df.empty:
        return "# Sales Data Analysis Report\n\nNo valid sales records were available after cleaning.\n"
    total_revenue = df["Total_Sales"].sum()
    average_sale = df["Total_Sales"].mean()
    highest_sale = df["Total_Sales"].max()
    lowest_sale = df["Total_Sales"].min()
    product_summary = df.groupby("Product", as_index=False).agg(
        Units_Sold=("Quantity", "sum"), Revenue=("Total_Sales", "sum")
    ).sort_values(["Revenue", "Units_Sold"], ascending=False)
    best_product = product_summary.iloc[0]
    region_summary = df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
    best_region = region_summary.index[0]
    lines = [
        "# Sales Data Analysis Report", "",
        "## Project overview",
        "This report summarizes the practice sales dataset using Python and pandas.", "",
        "## Data quality",
        f"- Rows in original CSV: {len(original)}",
        f"- Rows after cleaning: {len(df)}",
        f"- Exact duplicate rows removed: {len(original) - len(original.drop_duplicates())}",
        f"- Missing values remaining in cleaned data: {int(df.isna().sum().sum())}", "",
        "## Key metrics",
        f"- **Total revenue:** ₹{total_revenue:,.2f}",
        f"- **Average sale value:** ₹{average_sale:,.2f}",
        f"- **Highest individual sale:** ₹{highest_sale:,.2f}",
        f"- **Lowest individual sale:** ₹{lowest_sale:,.2f}",
        f"- **Total units sold:** {df['Quantity'].sum():,.0f}",
        f"- **Valid records:** {len(df)}", "",
        "## Best-selling product",
        f"- **Top product by revenue:** {best_product['Product']}",
        f"- Revenue: ₹{best_product['Revenue']:,.2f}",
        f"- Units sold: {best_product['Units_Sold']:,.0f}", "",
        "## Revenue by product", "| Product | Units sold | Revenue |", "|---|---:|---:|",
    ]
    for _, row in product_summary.iterrows():
        lines.append(f"| {row['Product']} | {row['Units_Sold']:,.0f} | ₹{row['Revenue']:,.2f} |")
    lines += ["", "## Revenue by region", "| Region | Revenue |", "|---|---:|"]
    for region, revenue in region_summary.items():
        lines.append(f"| {region} | ₹{revenue:,.2f} |")
    lines += [
        "", "## Method",
        "1. Loaded the CSV file using pandas.",
        "2. Checked required columns and converted numeric fields safely.",
        "3. Removed exact duplicate rows and records missing essential fields.",
        "4. Recalculated Total_Sales as Quantity multiplied by Unit_Price.",
        "5. Calculated summary metrics and grouped revenue by product and region.", "",
        "## Interpretation",
        f"The highest-revenue product is **{best_product['Product']}**. "
        f"The highest-revenue region is **{best_region}**. These findings describe this practice dataset only.", "",
        "## Limitations",
        "This is a sample learning dataset, not verified real business data.", ""
    ]
    return "\n".join(lines)


def main():
    """Run analysis and save the report."""
    original = load_data()
    cleaned = clean_data(original)
    REPORT_FILE.write_text(build_report(original, cleaned), encoding="utf-8")
    print("SALES DATA ANALYSIS")
    print("=" * 36)
    print(f"Original rows: {len(original)}")
    print(f"Clean rows: {len(cleaned)}")
    if cleaned.empty:
        print("No valid records to analyze.")
    else:
        print(f"Total revenue: ₹{cleaned['Total_Sales'].sum():,.2f}")
        print(f"Average sale: ₹{cleaned['Total_Sales'].mean():,.2f}")
        best = cleaned.groupby("Product")["Total_Sales"].sum().idxmax()
        print(f"Top product by revenue: {best}")
    print(f"Report saved to: {REPORT_FILE.name}")


if __name__ == "__main__":
    main()
