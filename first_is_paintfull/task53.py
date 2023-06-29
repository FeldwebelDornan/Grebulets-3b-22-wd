import os
class HomeToolList:
    def __init__(self):
        self.arr = []
        self.file = open('list.txt','w')
    def addTool(self,tool):
        self.arr.append(tool)
        self.file.write(tool+'\n')
    def delTool(self,tool):
        try:
            self.arr.remove(tool)
            self.file = None
            os.remove('list.txt')
            self.file = open('list.txt', 'w')
            for i in range(len(self.arr)):
                self.file.write(self.arr[i] + '\n')
        except Exception:
            print("такого дела нет в списке")
    def print(self):
        self.file = open('list.txt', 'r')
        res = [i.replace('\n', '') for i in self.file.readlines()]
        s = ''.join(i + ' ' for i in res)
        print(s)
list1 = HomeToolList()
list1.addTool('поесть')
list1.addTool('покурить')
list1.delTool('покурить')
list1.addTool('поспать')
list1.print()