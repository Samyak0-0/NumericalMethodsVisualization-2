import numpy as np

# Given data
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2.4, 3.1, 3.5, 4.2, 5.0, 6.0])

# Fit line y = a0 + a1*x using least squares
A = np.vstack([np.ones(len(x)), x]).T  # Design matrix
coeffs = np.linalg.lstsq(A, y, rcond=None)[0]  # [a0, a1]

a0, a1 = coeffs
print(f"a0 = {a0:.4f}, a1 = {a1:.4f}")

# Predict y at x = 2.5
x_predict = 2.5
y_predict = a0 + a1 * x_predict
print(f"Estimated y at x = {x_predict} is {y_predict:.4f}")
