def check_odd_even(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Test it
num = int(input("Enter a number: "))
print(check_odd_even(num))

