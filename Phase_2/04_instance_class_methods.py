# ==========================================
# Instance Method and Class Method
# ==========================================


class Employee:


    company = "Eduwings"


    def __init__(self,name):

        self.name = name



    # Instance Method
    # Object ke data ke saath kaam karta hai

    def show_name(self):

        print(
            f"Employee Name: {self.name}"
        )



    # Class Method
    # Class ke data ke saath kaam karta hai

    @classmethod
    def show_company(cls):

        print(
            f"Company Name: {cls.company}"
        )




employee1 = Employee("Gagan")


employee1.show_name()


Employee.show_company()