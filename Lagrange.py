x_values = [0,1,3,4,5]
y_values = [0,1,81,256,625]

value_to_find = 2

def small_l_x(i):
    
    temp = 1;
    for k in range(len(x_values)):
        if(i == k): continue;
        temp *= (value_to_find - x_values[k]) / (x_values[i] - x_values[k])
    return temp

def main():
    
    L_polynomial = 0
    for i in range(len(x_values)):
        L_polynomial += small_l_x(i) * y_values[i]
    
    print(f"\nUsing Lagrange Interpolation, The value of y({value_to_find}) is: {L_polynomial}.\n")

if __name__ == "__main__":
    main()
    