class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = int(age)

    def human_age(self):
        return self.age * self.age_factor
