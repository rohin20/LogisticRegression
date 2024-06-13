import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)
num_samples = 100
X = 2 * np.random.rand(num_samples, 1)
y = (X > 1).astype(int).ravel()  # Create a simple binary target variable

# Add bias term (intercept) to X
X_b = np.c_[np.ones((num_samples, 1)), X]

# Plot the data
plt.scatter(X, y, c=y, cmap='bwr')
plt.xlabel("X")
plt.ylabel("y")
plt.title("Sample Data")
plt.show()
