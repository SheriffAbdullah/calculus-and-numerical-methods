
def regula_falsi(f, x0, x1, decimals=4):
    def next_point(x0, x1):
        return x0 - ((x1 - x0) / (f(x1) - f(x0))) * f(x0)
        
    print(f"x0: {x0}")
    print(f"x1: {x1}")
    print(f"f(x0): {f(x0)}")
    print(f"f(x1): {f(x1)}\n")

    iteration = 1
    prev = x0
    curr = next_point(x0, x1)

    while round(prev, decimals + 1) != round(curr, decimals + 1):
        print(f"x{iteration} = {curr}")
        print(f"f(x{iteration}) = {f(curr)}")

        if f(curr) * f(x1) < 0:
            x0 = curr
            print(f"Root lies between {round(curr, decimals)} and {round(x1, decimals)}")
        elif f(curr) * f(x0) < 0:
            x1 = curr
            print(f"Root lies between {round(x0, decimals)} and {round(curr, decimals)}")
        else:
            print("Exact root found.")
            break

        print()
        prev = curr
        curr = next_point(x0, x1)
        iteration += 1

    print(f"\nHence, the root is {round(curr, decimals)}, correct to {decimals} decimal places.")


# Define the function and interval
def func(x):
    return x**3 - 9*x + 1

# Call the function
print("f(x) = x^3 - 9x + 1")
regula_falsi(func, x0=2, x1=4, decimals=4)
