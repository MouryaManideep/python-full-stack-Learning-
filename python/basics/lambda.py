people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Ravenclaw"},
    {"name": "Cho", "house": "Slytherin"}
]

# def f(person):
#     # return person["name"]
#     return person["house"]

# people.sort(key=f)


people.sort(key= lambda person: person["house"])

print(people)