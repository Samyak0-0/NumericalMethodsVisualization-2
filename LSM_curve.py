import numpy as np

x_values = np.array([2, 4, 6, 8, 10])
y_values = np.array([4.077, 11.084, 30.128, 81.897, 222.62])

x_value_to_estimate = 9

def main():
    
    # curve: y = a e^bx
    # ln Y = ln a + b x
    
    ln_Y = np.log(y_values)
    x_square = [x**2 for x in x_values]
    x_lnY = np.array(x_values * ln_Y)
    
    linear_eqn = np.array([[len(x_values), np.sum(x_values)], [np.sum(x_values), np.sum(x_square)]])
    coefficents = np.array([np.sum(ln_Y), np.sum(x_lnY)])
    
    ln_a, b = np.linalg.solve(linear_eqn, coefficents)
    a = np.exp(ln_a)
    y_estimate = a * np.exp(b * x_value_to_estimate)

    print(f"\na = {a:.4f}, b = {b:.4f}")
    print(f"y(x) = {a:.4f} * e ^({b:.4f} * x)")
    print(f"\nEstimated value of y at x = {x_value_to_estimate} is : {y_estimate:.4f} \n")
    

    
if __name__ == "__main__":
    main()