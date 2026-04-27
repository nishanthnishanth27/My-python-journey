def get_factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * get_factorial(n - 1)

# Get user input
try:
    num = int(input("Enter a number: "))
    print(f"The factorial of {num} is {get_factorial(num)}")
except ValueError:
    print("Please enter a valid integer.")

