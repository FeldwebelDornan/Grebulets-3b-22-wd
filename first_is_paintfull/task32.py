class schoolboy:
    def __init__(self,name,clas):
        self.name = name
        self.clas = clas
    def ucheba(self):
        print(f'{self.name} из {self.clas} учится')
vasya = schoolboy('вася','11А')
vasya.ucheba()