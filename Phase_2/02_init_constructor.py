# ==========================================
# __init__ Constructor
# ==========================================


# __init__ automatically run hota hai
# jab object create hota hai


class Student:


    # Constructor
    def __init__(self, name, age, course):

        # Object ke andar data save kar rahe hain

        self.name = name
        self.age = age
        self.course = course



# Object banate time values pass karenge

student1 = Student(
    "Gagan",
    22,
    "Python"
)


student2 = Student(
    "Rahul",
    21,
    "AI"
)



print(student1.name)
print(student1.course)


print(student2.name)
print(student2.course)