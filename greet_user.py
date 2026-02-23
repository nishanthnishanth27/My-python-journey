# A simple program to greet the user and check their age
name = input("Enter your name: ")
print("Hello, " + name + "!")

age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are still a minor.")

print("Thanks for using my script!")

