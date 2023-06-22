class Student:
    def __init__(self,name,surname,age,spetska):
        self.name = name
        self.surname = surname
        self.age = age
        self.spetska = spetska
    def vivod(self):
        print(f'{self.name} - {self.surname} {self.age} {self.spetska}')