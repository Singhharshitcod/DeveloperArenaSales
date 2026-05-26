# Sales Data Analysis Report

## Overview
This report outlines the key findings from the recent sales data analysis. The data was processed using Python's `pandas` library, ensuring data integrity by checking and appropriately handling any missing values. 

## Key Metrics Calculated

Based on the data in `sales_data.csv`, we have extracted the following critical business metrics:

### 1. Total Revenue
The total generated revenue across all products and regions is **$12,365,048.00**.

### 2. Top Selling Product
The most popular product among our customers, based on total quantity sold, is the **Laptop**. 

### 3. Average Order Value (AOV)
The average transaction size across all recorded sales is **$123,650.48**. 

## Methodology
- **Data Loading:** Loaded raw CSV data into a pandas DataFrame.
- **Data Cleaning:** Verified the dataset for `NaN` or `Null` values. No missing values were detected in the provided dataset, ensuring the calculations are based on complete records. 
- **Aggregation:** Grouped data by product and region to calculate sales velocity and regional performance. 

## File Structure
- `sales_analysis.py`: Contains the logic for data cleaning, missing value handling, and metric aggregation.
- `sales_data.csv`: The raw dataset containing Date, Product, Quantity, Price, Customer ID, Region, and Total Sales.
- `analysis_report.md`: This summary document.