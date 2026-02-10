class Student:
    child = 0
    adult = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.count()

    def introduce(self):
        print(f"Hi! My Name is {self.name} and I am {self.age} Years Old.")

    def count(self):
        if(self.age >=19):
            Student.adult += 1
        else:
            Student.child += 1


    @classmethod
    def about(cls):
        print(f"There are {Student.adult} adults and {Student.child} children.")


p1 = Student("man",35)
p2 = Student("boy",14)
p3 = Student("girl", 12)
p4 = Student("woman",31)

p1.introduce()
p2.introduce()
p3.introduce()
p4.introduce()
Student.about()