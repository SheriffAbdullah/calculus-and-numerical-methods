import math
import numpy as np

def numerical_integration(func, lower_limit=0, upper_limit=1, step_size=0.25, rule='simpson_1_3'):
    def trapezoid(y):
        return (step_size / 2) * (y[0] + y[-1] + (2 * sum(y[1:-1])))

    def simpson_1_3(y):
        n = len(y) - 1
        if n % 2 != 0:
            raise ValueError("Simpson's 1/3 rule requires an even number of intervals.")
        remaining = sum(y[1:-1]) - sum(y[2:-1:2])
        return (step_size / 3) * (y[0] + y[-1] + (2 * sum(y[2:-1:2])) + (4 * remaining))

    def simpson_3_8(y):
        n = len(y) - 1
        if n % 3 != 0:
            raise ValueError("Simpson's 3/8 rule requires number of intervals to be a multiple of 3.")
        remaining = sum(y[1:-1]) - sum(y[3:-1:3])
        return (3 * step_size / 8) * (y[0] + y[-1] + (2 * sum(y[3:-1:3])) + (3 * remaining))

    # Use linspace to avoid floating point error accumulation
    num_points = int(round((upper_limit - lower_limit) / step_size)) + 1
    x_ = np.linspace(lower_limit, upper_limit, num_points)
    y_ = [func(x) for x in x_]

    print("(x, y)")
    for i in zip(x_, y_):
        print(i)
    print()

    print(f"Area of integral: ", end="")
    if rule == 'trapezoid':
        print(trapezoid(y_))
        print("by Trapezoid rule.")
    elif rule == 'simpson_1_3':
        print(simpson_1_3(y_))
        print("by Simpson's 1/3rd rule.")
    elif rule == 'simpson_3_8':
        print(simpson_3_8(y_))
        print("by Simpson's 3/8th rule.")
    else:
        raise Exception("Invalid rule. Please enter a valid rule.")

def func(x):
    return np.sqrt(25 * (np.sin(x)**2) + 9 * (np.cos(x)**2))

lower_limit = 0
upper_limit = 2 * np.pi
step_size = np.pi / 4

print("f(x) = sqrt(25*sin^2(x) + 9*cos^2(x))")
print(f"Lower limit (a): {lower_limit}")
print(f"Upper limit (b): {upper_limit}")
print(f"Step size (h): {step_size}")
print()

numerical_integration(func, lower_limit, upper_limit, step_size, rule='trapezoid')
