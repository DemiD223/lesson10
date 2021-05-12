class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def talk(self):
        print(f"Hello my name is {self.fname} {self.lname} and I'm {self.age} years old")
