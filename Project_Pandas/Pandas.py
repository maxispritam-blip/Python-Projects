import pandas as pd

# Load a CSV file into a DataFrame

df = pd.read_csv('sales_data.csv')
print(df.head())

# Check for missing values in the DataFrame

df.isnull().sum()

# convert a column to datetime format

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
print(df.dtypes)

# Calculate the total sales and total profit by region

region_summary = df.groupby('Region').agg({'Sales_Amount': 'sum', 'Profit': 'sum'})
print(region_summary)

# Average sales amount by product category

avg_sales = df.groupby('Product_Category')['Sales_Amount'].mean()
print(avg_sales)

# Top 5 orders by sales amount

top_orders = df.groupby('Order_ID')['Sales_Amount'].sum().nlargest(5)
print(top_orders)

# Summary report of sales and profit by region

region_summary.to_csv('region_summary_report.csv')