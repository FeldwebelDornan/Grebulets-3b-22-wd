class character:
    def __init__(self,name,level,health:float,damage:float,defence):
        self.name = name
        self.level = level
        self.health = health
        self.damage = damage
        self.defence = defence
    def __str__(self):
        return f'{self.name}:\nlvl {self.level}\nhp {round(self.health,2)}\ndmg {round(self.damage,2)}\ndefence {self.defence}'
def attack(atacker:character,defender:character):
    defender.health-=atacker.damage - atacker.defence
def lvlup(pers:character):
    pers.level+=1
    pers.health*=1.1
    pers.damage*=1.1
def winner(pers1:character,pers2:character):
    print(f'победил {pers1.name}') if pers1.health>pers2.health else print(f'победил {pers2.name}')
a = character('biba',10,10,4,2)
b = character('boba',4,8,2,1)
print(a)
print(b)
for i in range(3):
    print(f'{i+1} round')
    attack(a, b)
    attack(b, a)
    winner(a,b)
    lvlup(b)
    print(a)
    print(b)
winner(a,b)