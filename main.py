import numpy as np
import matplotlib.pyplot as plt

def plot_linear(m, b):
    x = np.linspace(0, 50, 100)
    y = m * x + b
    plt.plot(x, y, label=f'y = {m}x + {b}')
    
def plot_quadratic(a, b, c):
    x = np.linspace(0, 50, 100)
    y = a * x**2 + b * x + c
    plt.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
    
def plot_cubic(a, b, c, d):
    x = np.linspace(0, 50, 100)
    y = a * x**3 + b * x**2 + c * x + d
    plt.plot(x, y, label=f'y = {a}x³ + {b}x² + {c}x + {d}')

def main():
    print("Choose the type of equation to plot:")
    print("1. Linear (y = mx + b)")
    print("2. Quadratic (y = ax² + bx + c)")
    print("3. Cubic (optional, y = ax³ + bx² + cx + d)")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        m = float(input("Enter the coefficient m (slope): "))
        b = float(input("Enter the coefficient b (y-intercept): "))
        plot_linear(m, b)
        
    elif choice == '2':
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the coefficient b: "))
        c = float(input("Enter the coefficient c: "))
        plot_quadratic(a, b, c)
        
    elif choice == '3':
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the coefficient b: "))
        c = float(input("Enter the coefficient c: "))
        d = float(input("Enter the coefficient d: "))
        plot_cubic(a, b, c, d)
        
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        return

    plt.title('Plot of the Chosen Equation')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.legend()
    plt.grid()
    plt.xlim(0, 50)
    plt.ylim(bottom=0)  # Ensures the y-axis starts from 0
    plt.show()

if __name__ == '__main__':
    main()
