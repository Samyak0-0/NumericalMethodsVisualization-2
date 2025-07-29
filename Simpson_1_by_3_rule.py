import numpy as np

def y_function(x):
    return np.exp(-(x**2)/2)

def main():
    
    no_of_steps = 50;
    x_values = np.linspace(-4,4, no_of_steps+1)
    y_values = np.round(y_function(x_values), 4)
    
    integral = 0
    for i in range(len(x_values)):
        if(i==0 or i == len(x_values)):
            integral += y_values[i];
        elif (i%2==0):
            integral += 2*y_values[i];
        else:
            integral += 4*y_values[i];

    integral *= abs(-4-4)/no_of_steps
    integral /= 3
    integral *= (1/(2*np.pi))**0.5
    
        
    print(f"\nFrom Simpson 1/3 Rule, I = √(1/2π) ∫ e^(-x^2/2)dx in [-4,4] is {integral:.4f}.\n")

if __name__ == "__main__":
    main()