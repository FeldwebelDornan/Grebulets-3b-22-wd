class Student:
    def __init(self,name,surname,curs,firstsub,secondsub):
        self.name = name
        self.surname = surname
        self.curs = curs
        self.firstsub = firstsub
        self.secondsub = secondsub
    def midscore(self):
        return (self.firstsub+self.secondsub)/2