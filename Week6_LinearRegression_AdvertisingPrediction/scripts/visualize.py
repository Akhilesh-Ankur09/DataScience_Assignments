import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.linear_model import LinearRegression

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "advertising.csv"

df = pd.read_csv(DATA_PATH)

X = df[['TV']]
y = df['Sales']

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

# Plot 1: Distribution of TV Budget
plt.figure()
plt.hist(df['TV'], bins=20)
plt.xlabel("TV Advertising Budget")
plt.ylabel("Frequency")
plt.title("Distribution of TV Advertising Budget")
plt.show()

# Plot 2: Distribution of Sales
plt.figure()
plt.hist(df['Sales'], bins=20)
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.title("Distribution of Sales")
plt.show()

# Plot 3: TV vs Sales with Regression Line
plt.figure()
plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_pred, label="Regression Line")
plt.xlabel("TV Advertising Budget")
plt.ylabel("Sales")
plt.title("TV Advertising vs Sales (Linear Regression)")
plt.legend()
plt.show()

# Plot 4: Residual Plot
residuals = y - y_pred

plt.figure()
plt.scatter(y_pred, residuals)
plt.axhline(0)
plt.xlabel("Predicted Sales")
plt.ylabel("Residual Error")
plt.title("Residual Plot")
plt.show()

# Plot 5: Actual vs Predicted Sales
plt.figure()
plt.scatter(y, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.show()

print("All visualizations generated successfully.")