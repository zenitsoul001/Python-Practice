# ==========================================
# Basic Inheritance
# ==========================================


# Parent Class

class Animal:


    def eat(self):

        print(
            "Animal is eating"
        )



# Child Class
# Animal ke features inherit karega


class Dog(Animal):


    def bark(self):

        print(
            "Dog is barking"
        )



dog1 = Dog()


# Parent method access

dog1.eat()


# Own method

dog1.bark()