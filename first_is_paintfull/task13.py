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