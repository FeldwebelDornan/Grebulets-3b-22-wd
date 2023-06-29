class Card:
    def __init__(self,name,cost,kolvo):
        self.name = name
        self.__cost = cost
        self.__kolvo = kolvo
    def minuscost(self,dif:int):
        if self.__cost>=dif:
            self.__cost-=dif
        else:
            print("цена не может быть отрицательной")
            exit()
    def minuskolvo(self,dif:int):
        if self.__kolvo>=dif:
            self.__kolvo-=dif
        else:
            print("количество не может быть отрицательным")
            exit()
    def __str__(self):
        return f'{self.name}: {self.__kolvo} осталось по цене {self.__cost}р за шутку'
