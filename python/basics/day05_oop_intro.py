# class Student:
#     child = 0
#     adult = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.count()

#     def introduce(self):
#         print(f"Hi! My Name is {self.name} and I am {self.age} Years Old.")

#     def count(self):
#         if(self.age >=19):
#             Student.adult += 1
#         else:
#             Student.child += 1


#     @classmethod
#     def about(cls):
#         print(f"There are {Student.adult} adults and {Student.child} children.")


# p1 = Student("man",35)
# p2 = Student("boy",14)
# p3 = Student("girl", 12)
# p4 = Student("woman",31)

# p1.introduce()
# p2.introduce()
# p3.introduce()
# p4.introduce()
# Student.about()

# class Point():
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2

# p = Point(2, 3)
# print(p.x)
# print(p.y)

# class Flight():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []
    
#     def add_passengers(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True

#     def open_seats(self):
#         return self.capacity - len(self.passengers)
    

# flight = Flight(3)
# people = ["Harry", "Ron", "Hermione", "Ginny"]

# for person in people:
    
#     if flight.add_passengers(person):
#         print(f"Added {person} to flight successfully.")
#     else:
#         print(f"No available seats for {person}.")