# Day 2: Conditions in Python

number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is a Positive number")
elif number < 0:
    print(f"{number} is a Negative number")
else:
    print("Zero")


# Even or odd check
if number % 2 == 0:
    print(f"{number} is a Even number")
else:
    print(f"{number} is a Odd number")

"""Problem"""

# Eligible of vote
if number>=18:
    print("You are eligible of vote!")
elif number>=14 and number<18:
    print("Wait for your teenage to complte")
else:
    print(f"Return to the next elections after {18-number} years!")
