# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:47:28 2024

@author: mcall
"""

import pandas as pd
import numpy as np

# Define the size of the dataset
num_rows = 1000000  # 1 million rows

# Generate synthetic financial data
np.random.seed(42)
quarters = np.arange(1, num_rows + 1)
revenue = np.random.uniform(10000, 100000, size=num_rows)  # Random revenue between 10,000 and 100,000
expenses = np.random.uniform(5000, 70000, size=num_rows)  # Random expenses between 5,000 and 70,000
profit = revenue - expenses

# Create a DataFrame
financial_data = pd.DataFrame({
    'Quarter': quarters,
    'Revenue': revenue,
    'Expenses': expenses,
    'Profit': profit
})

# Save the financial data to a CSV file
financial_data.to_csv('financial_data.csv', index=False)
