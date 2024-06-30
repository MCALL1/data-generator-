# -*- coding: utf-8 -*-
""
"Smample maketing data"


import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(0)  # for reproducibility

# Number of data points
n_points = 100

# Sample data for marketing expenses and revenues
marketing_expense = np.random.uniform(10, 100, n_points)
revenue = marketing_expense * np.random.uniform(0.5, 1.5, n_points)

# Geographic coordinates (assuming a specific region for simplicity)
latitude = np.random.uniform(40.5, 41.0, n_points)
longitude = np.random.uniform(-74.5, -74.0, n_points)

# Create DataFrame
data = pd.DataFrame({
    'Marketing Expense': marketing_expense,
    'Revenue from Campaign': revenue,
    'Latitude': latitude,
    'Longitude': longitude
})

# Save to CSV file
data.to_csv('marketing_data.csv', index=False)

print("Sample marketing data saved to 'marketing_data.csv'.")
