#Write a Python program to import built-in array module and display the namespace of the said module
import array
for name in array.__dict__:
    print(name)

#Write a Python program to create a class and display the namespace of the said class

class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]
for name in py_solution.__dict__:
    print(name)

#Write a Python program to create an instance of a specified class and display the namespace of the said instance

class Person:
    def __init__(self, Name, Employement, Place, Age):
        self.Name = Name
        self.Employement = Employement
        self. Place = Place
        self.Age = Age

    def displaydetails(self):
        print("The emplyees name and details are: ", self.Name, self.Employement, self. Place, self.Age)

Person1 = Person("shana", "Engineer", "Sweden", 34)
Person1.displaydetails()
