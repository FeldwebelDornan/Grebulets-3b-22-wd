class Worker:
    def __init__(self,name,cast,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.cast = cast
    def predstavlenie(self):
        print(f'имя {self.name}-{self.cast}, возраст:{self.age}, зарплата: {self.salary}')
down = Worker('Васёк','заводчанин','45',15000)
down.predstavlenie()