class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def square(self):
        return self.length * self.width
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print(self):
        print(self.name)
        print(self.age)
class Dog:
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age
    def print(self):
        print(self.name)
        print(self.breed)
        print(self.age)
class Student:
    def __init(self,name,surname,curs,firstsub,secondsub):
        self.name = name
        self.surname = surname
        self.curs = curs
        self.firstsub = firstsub
        self.secondsub = secondsub
    def midscore(self):
        return (self.firstsub+self.secondsub)/2
class BankAccaunt:
    def __init__(self,username,scorenumber,balance):
        self.username = username
        self.scorenumber = scorenumber
        self.balance = balance
    def additting(self,a):
        self.balance+= a
        return self.balance
    def debt(self,a):
        self.balance -= a
        return self.balance
