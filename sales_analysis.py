import pandas as pd

def analyze_sales_data(filepath):
    print(f"Loading data from {filepath}...")
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print("Error: File not found. Please ensure 'sales_data.csv' is in the directory.")
        return

    # Checking and handle for missing values
    missing_values = df.isnull().sum().sum()
    if missing_values > 0:
        print(f"Found {missing_values} missing values. Dropping incomplete rows...")
        # you could use df.fillna() depending on business logic
        df = df.dropna()
    else:
        print("No missing values found.")


    # Metric 1: Total Revenue
    total_revenue = df['Total_Sales'].sum()

    # Metric 2: Top Selling Product (by total quantity sold)
    top_product = df.groupby('Product')['Quantity'].sum().idxmax()
    top_product_qty = df.groupby('Product')['Quantity'].sum().max()

    # Metric 3: Average Order Value (AOV)
    avg_order_value = df['Total_Sales'].mean()
    
    # Metric 4: Sales by Region
    sales_by_region = df.groupby('Region')['Total_Sales'].sum().to_dict()

    print("\n--- Analysis Complete ---")
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Top Selling Product: {top_product} ({top_product_qty} units)")
    print(f"Average Order Value: ${avg_order_value:,.2f}")
    
    return {
        "total_revenue": total_revenue,
        "top_product": top_product,
        "avg_order_value": avg_order_value,
        "sales_by_region": sales_by_region
    }

if __name__ == "__main__":
    analyze_sales_data('task3/sales_data.csv')