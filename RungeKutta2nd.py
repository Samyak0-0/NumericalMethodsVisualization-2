import numpy as np

def f(x,y):
    return x**2+x;

def main():
    
    x0 = 0
    y0 = 1
    
    h = (2-x0)/10
    
    print("\nApproximation of y(x) using Runge-Kutta 2nd method:")
    print("------------------------------------------")
    print("  i   |    x_i    |     y_i")
    print("------------------------------------------")
    print(f"   0  |     {x0}     |    {y0:.4f}")
    
    x = x0;
    y = y0;
    i=0
    while x<1.9:
      k1 = h * f(x, y)
      k2 = h * f(x + h, y + k1)
      y += (k1 + k2) / 2
      x += h
      i += 1
      print(f"  {i:2d}  |    {x:.1f}    |    {y:.4f}")
        
        
    print(f"\nThe approximate value of y(2) is: {y:.4f}")
   
    
if __name__ == "__main__":
    main();