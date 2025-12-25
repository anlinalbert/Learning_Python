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

Filter the data to show only days where Sales_USD was greater than $150.

NumPy: * Convert the Sales_USD column into a NumPy array.

Use a NumPy function to calculate the standard deviation of the sales.

Matplotlib/Seaborn: * Create a line plot showing the Sales_USD over the days of the week.

Add a title ("Weekly Sales Trend") and label your axes.
"""