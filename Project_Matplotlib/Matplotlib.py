import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load Dataset

data = pd.read_csv('monthly_revenue.csv')

# line Chart Showing Monthly Revenue for Three Products

plt.figure(figsize=(12, 4))
plt.plot(data['Month'], data['Product_A_Revenue'], marker='o', label='Product A')
plt.plot(data['Month'], data['Product_B_Revenue'], marker='s', label='Product B')
plt.plot(data['Month'], data['Product_C_Revenue'], marker='^', label='Product C')
plt.title('Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.legend()
plt.grid(True)
plt.show()

# Bar Chart Showing Total Annual Revenue for Each Product

plt.figure(figsize=(12, 4))
plt.bar(data['Month'], data['Product_A_Revenue'], label='Product A')
plt.bar(data['Month'], data['Product_B_Revenue'], label='Product B')
plt.bar(data['Month'], data['Product_C_Revenue'], label='Product C')
plt.title('Total Annual Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.legend()
plt.show()

# stacked area chart Showing Monthly Revenue Distribution

plt.figure(figsize=(12, 4))
plt.stackplot(data['Month'], 
              data['Product_A_Revenue'], 
              data['Product_B_Revenue'], 
              data['Product_C_Revenue'], 
              labels=['Product A', 'Product B', 'Product C'], alpha=0.5)
plt.title('Stacked Area Chart of Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()