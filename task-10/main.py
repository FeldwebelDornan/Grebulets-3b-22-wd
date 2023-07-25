class Student:
    def __init__(self,name,surname,age,spetska):
        self.name = name
        self.surname = surname
        self.age = age
        self.spetska = spetska
    def vivod(self):
        print(f'{self.name} - {self.surname} {self.age} {self.spetska}')
class Avto:
    def __init__(self,mark,model,seriesyear,cost):
        self.mark = mark
        self.model = model
        self.seriesyear = seriesyear
        self.cost = cost
    def vivod(self):
        print(f'{self.mark}-{self.model}, {self.seriesyear}, {self.cost}')
class Cat:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def vivod(self):
        print(f'Кошка по имени {self.name}, {self.age}, цвет {self.color}')
class Book:
    def __init(self,name,author,year,genre):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
    def vivod(self):
        print(f'{self.name}, {self.author}({self.year}), {self.genre}')
class GeomFigure:
    def __inti__(self,square,perimetr):
        self.square = square
        self.perimetr = perimetr
    def vivod(self):
        print(f'площадь - {self.square}, периметр - {self.perimetr}')