# ==========================================
# self Keyword
# ==========================================


# self current object ko represent karta hai


class Employee:


    def __init__(self,name,salary):

        # self.name means
        # is object ka name

        self.name = name
        self.salary = salary



    def show_details(self):

        print(
            f"Name: {self.name}"
        )

        print(
            f"Salary: {self.salary}"
        )



employee1 = Employee(
    "Gagan",
    50000
)


employee2 = Employee(
    "Aman",
    40000
)



employee1.show_details()

print("----------------")

employee2.show_details()