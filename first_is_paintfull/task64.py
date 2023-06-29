class Client:
    def __init__(self,name,size):
        self.name = name
        self.size = size
    def __str__(self):
        return f'{self.name} имеет {self.size} в наличии'
class Bank:
    def __init__(self):
        self.clients = []
        self.tranz = []
    def createClient(self,client:Client):
        self.clients.append(client)
    def tranzaktion(self, name1, name2,sum):
        for i in self.clients:
            if i.name == name1:
                a = i
                break
        for i in self.clients:
            if i.name == name2:
                b = i
                break
        if a.size<sum:
            print('недостаточно денег')
            exit()
        else:
            a.size-=sum
            b.size+=sum
            self.tranz.append(f'{name1} передал {name2}: {sum}')
    def ptr(self):
        for i in self.clients:
            print(str(i))
        print(self.tranz)
Sber = Bank()
ivan = Client('Иван',10000)
masha = Client('Маша',50)
Sber.createClient(ivan)
Sber.createClient(masha)
Sber.tranzaktion('Иван','Маша',5000)
Sber.tranzaktion('Маша','Иван',50)
Sber.ptr()


