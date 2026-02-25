# Day 4: Working with decimals (float)
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (years): "))

interest = (p * r * t) / 100
print(f"Your Simple Interest is: {interest}")
