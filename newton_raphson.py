import math

def newton_raphson(f, f_derivative, x0, decimals=3, tolerance=1e-10):
    def next_point(x):
        derivative = f_derivative(x)
        if derivative == 0:
            raise ZeroDivisionError(f"f'({x}) = 0. Cannot divide by zero.")
        return x - f(x) / derivative

    print(f"Initial guess, x0: {x0}")
    print(f"f(x0): {round(f(x0), decimals)}")
    print(f"f'(x0): {round(f_derivative(x0), decimals)}\n")

    prev = x0
    try:
        curr = next_point(prev)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return

    iteration = 1

    while round(curr, decimals+1) != round(prev, decimals+1):
        print(f"Iteration {iteration}:")
        print(f"  x{iteration} = {round(curr, decimals)}")
        print(f"  f(x{iteration}) = {round(f(curr), decimals)}\n")
        
        prev = curr
        try:
            curr = next_point(curr)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            return
        iteration += 1

    print(f"Hence, the root is approximately {round(curr, decimals)}, correct to {decimals} decimal places.")

def func(x):
    return math.cos(x) - x * math.exp(x)

def func_derivative(x):
    return -math.sin(x) - math.exp(x) * (x + 1)

print("f(x) = cos(x) - x·e^x")
print("f'(x) = -sin(x) - e^x·(1 + x)\n")
newton_raphson(func, func_derivative, x0=1, decimals=4)
