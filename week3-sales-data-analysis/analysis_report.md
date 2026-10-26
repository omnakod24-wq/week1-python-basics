# Sales Data Analysis Report

## Project overview
This beginner project uses pandas to explore and analyze a 100-row practice sales dataset.

## Setup
1. Install Python 3.
2. Open a terminal in this folder.
3. Install dependencies: `py -m pip install -r requirements.txt` on Windows, or `python3 -m pip install -r requirements.txt`.
4. Run: `py sales_analysis.py` on Windows, or `python3 sales_analysis.py`.
5. The script updates this report with the latest calculated metrics.

## Dataset
- Data rows: 99
- Columns: Product, Quantity, Unit_Price, Total_Sales, Region
- Products: Notebook, Pen, Backpack, Water Bottle, Calculator
- Regions: West, North, South, East

## Key findings from the supplied CSV
- **Total revenue:** ₹1,67,930.00
- **Average sale value:** ₹1,696.26
- **Highest individual sale:** ₹5,950.00
- **Lowest individual sale:** ₹250.00
- **Total units sold:** 1602
- **Best product by revenue:** Backpack (₹68,000.00)
- **Highest-revenue region:** South (₹46,190.00)

## Revenue by product
| Product | Revenue |
|---|---:|
| Backpack | ₹68,000.00 |
| Calculator | ₹40,050.00 |
| Water Bottle | ₹32,220.00 |
| Notebook | ₹18,900.00 |
| Pen | ₹8,760.00 |

## Revenue by region
| Region | Revenue |
|---|---:|
| South | ₹46,190.00 |
| West | ₹42,250.00 |
| North | ₹41,060.00 |
| East | ₹38,430.00 |

## Analysis steps
1. Read the CSV using pandas.
2. Validate required columns and convert numeric columns safely.
3. Remove exact duplicate rows and rows missing essential product, quantity, or unit price values.
4. Recalculate revenue as quantity multiplied by unit price.
5. Calculate total, average, maximum, minimum, total units, product revenue, and region revenue.
6. Write the results to this Markdown report.

## Code structure
- sales_analysis.py: loading, cleaning, analysis, and report generation.
- sales_data.csv: 100-row practice dataset.
- analysis_report.md: generated report and documentation.
- requirements.txt: pandas dependency.
- test_cases.txt: test checklist.
- screenshots/: visual documentation guidance and illustrative preview.

## Testing
See test_cases.txt for expected checks covering row count, revenue calculations, duplicates, missing values, and report generation.

## Visual documentation
The screenshots folder contains an illustrative preview. For final submission, run the program locally and add a real terminal screenshot.
