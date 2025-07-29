import numpy as np

x_values = [1, 2, 3, 4, 5, 6]
y_values = [2.4, 3.1, 3.5, 4.2, 5.0, 6.0]

value_to_estimate = 2.5

def main():
    
    x_square = [x**2 for x in x_values]
    xy = []
    for i in range(len(x_values)):
        xy.append(x_values[i]*y_values[i])
    print(xy)
    
if __name__ == "__main__":
    main()