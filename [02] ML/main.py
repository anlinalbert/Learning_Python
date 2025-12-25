"""
The Challenge: "The Coffee Shop Analysis"
You have been given a small dataset of coffee shop sales. Your goal is to process this data, calculate some statistics,
and visualize the results.

Copy and paste this code to create your starting point:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary of data
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Sales_USD': [120, 150, 90, 200, 210, 350, 400],
    'Customers': [30, 35, 20, 45, 50, 80, 95]
}

# Your Task Starts Here:
# 1. Convert the dictionary into a Pandas DataFrame.

2. Your Tasks
Pandas: * Add a new column called Average_Spend by dividing Sales_USD by Customers.

Filter the data to show only days when Sales_USD was greater than $150.

NumPy: * Convert the Sales_USD column into a NumPy array.

Use a NumPy function to calculate the standard deviation of the sales.

Matplotlib/Seaborn: * Create a line plot showing the Sales_USD over the days of the week.

Add a title ("Weekly Sales Trend") and label your axes.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary of data
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Sales_USD': [120, 150, 90, 200, 210, 350, 400],
    'Customers': [30, 35, 20, 45, 50, 80, 95]
}

# Task 1 completed
pandas_df = pd.DataFrame(data)

# Task 2 add column
pandas_df["Average_Spend"] = pandas_df["Sales_USD"] / pandas_df["Customers"]

# Task 2 filter
print(pandas_df.query("Sales_USD > 150"))

# Task 2 convert to numpy array and find sd
sales_USD = pandas_df["Sales_USD"].values
print(f"Standard deviation = {np.std(sales_USD)}")

# Task 2 matplotlib
# Set the visual style using Seaborn
sns.set_theme(style="whitegrid")

# Create the plot
plt.figure(figsize=(10, 5))
sns.lineplot(x='Day', y='Sales_USD', data=pandas_df, marker='o', color='b')

# Customize using Matplotlib
plt.title('Weekly Sales Trend', fontsize=16)
plt.xlabel('Day of the Week')
plt.ylabel('Sales (USD)')

# Show the plot
plt.show()