class Avto:
    def __init__(self,mark,model,seriesyear,cost):
        self.mark = mark
        self.model = model
        self.seriesyear = seriesyear
        self.cost = cost
    def vivod(self):
        print(f'{self.mark}-{self.model}, {self.seriesyear}, {self.cost}')