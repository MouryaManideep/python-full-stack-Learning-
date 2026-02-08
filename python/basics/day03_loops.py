# Day 3: Loops in Python

number = int(input("What is the numnber? "))

for i in range(1, number+1):
    print(f"User Aske dme to print 1 - {number}",end=" ")

sum = 0
for i in range(1, number+1):
    sum += i
print(f"Sum Natural number from 1 - {number} is =",sum)

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