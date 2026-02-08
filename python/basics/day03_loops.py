# Day 3: Loops in Python

number = int(input("What is the numnber? "))

print(f"User Asked to print 1 - {number} :",end=" ")
for i in range(1, number+1):
    print(i,end=" ")
print()

sum = 0
for i in range(1, number+1):
    sum += i
print(f"Sum of Natural number from 1 - {number} is =",sum)

count = 5
while (count >= 0):
    if(count != 0):
        print(f"Next run starts in {count}sec..")
    else:
        print("Initialising. . . . .")
    count -= 1

e = 1
print(f"User {number} Table. . . ")
while e <=10:
    print(f"{number} x {e} = {number*e}")
    e += 1

space = number
star = 1
"""Pyramid"""
print(f"Pyramid with {number} rows. :")
for i in range(1, number+1):
    space -= 1
    print(" " * space + "*" * star)
    star = (2*i)+1