# Sales Data Analysis Report

## Project overview
This beginner project uses pandas to explore and analyze a 100-row practice sales dataset. Run sales_analysis.py to generate current metrics from sales_data.csv.

## Setup
1. Install Python 3.
2. Open a terminal in this folder.
3. Install dependencies with: py -m pip install -r requirements.txt (Windows), or python3 -m pip install -r requirements.txt.
4. Run the analysis with: py sales_analysis.py (Windows), or python3 sales_analysis.py.

## Analysis steps
- Read the CSV with pandas.
- Check required columns and clean data.
- Remove duplicate rows and rows missing essential product, quantity, or price data.
- Recalculate revenue as quantity multiplied by unit price.
- Calculate total revenue, average sale, highest and lowest sale, total units, product revenue, and region revenue.

## Code structure
- sales_analysis.py: loading, cleaning, analysis, and report generation.
- sales_data.csv: 100-row practice dataset.
- analysis_report.md: generated Markdown report and documentation.
- requirements.txt: pandas dependency.
- test_cases.txt: testing checklist.
- screenshots/: visual documentation guidance and illustrative preview.

## Testing
Follow test_cases.txt for expected checks including CSV row count, revenue calculation, duplicate handling, missing values, and report generation.

## Visual documentation
The screenshots folder contains an illustrative preview. For final evidence, run the script locally and add a real terminal screenshot.
