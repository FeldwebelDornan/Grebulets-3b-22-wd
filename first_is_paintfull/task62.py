import time
class Robot:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
    def moving(self):
        for i in range(10):
            print(i*self.speed)
            time.sleep(1)
class GusenichniyRobot(Robot):
    def __init__(self,name,speed,territoriya):
        Robot.__init__(self,name,speed)
        self.terr = territoriya

class RobotNaKolyosah(Robot):
    def __init__(self,name, speed, mark):
        Robot.__init__(self, name, speed)
        self.mark = mark
