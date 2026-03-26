# House Price Prediction using Linear Regression

import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data (Area in sq.ft vs Price)
area = np.array([500, 1000, 1500, 2000, 2500]).reshape(-1, 1)
price = np.array([100000, 200000, 300000, 400000, 500000])

# Train model
model = LinearRegression()
model.fit(area, price)

# Predict price for new area
new_area = [[1800]]
predicted_price = model.predict(new_area)

print("Predicted price for 1800 sq.ft:", predicted_price[0])