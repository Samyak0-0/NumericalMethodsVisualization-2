import numpy as np

x_values = np.array([1, 2, 3, 4, 5, 6])
y_values = np.array([2.4, 3.1, 3.5, 4.2, 5.0, 6.0])

x_value_to_estimate = 2.5

def main():
    
    x_square = [x**2 for x in x_values]
    xy = np.array(x_values * y_values)
    
    linear_eqn = np.array([[len(x_values), np.sum(x_values)], [np.sum(x_values), np.sum(x_square)]])
    coefficents = np.array([np.sum(y_values), np.sum(xy)])
    
    a0, a1 = np.linalg.solve(linear_eqn, coefficents)
    y_estimate = a0 + a1 * x_value_to_estimate
    
    print(f"a0 = {a0:.4f}, a1 = {a1:.4f}")
    print(f"y(x) = {a0:.4f} + {a1:.4f} * x")
    print(f"\nEstimated y at x = {x_value_to_estimate} is : {y_estimate:.4f} \n")
    

    
if __name__ == "__main__":
    main()