class Book:
    def __init(self,name,author,year,genre):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
    def vivod(self):
        print(f'{self.name}, {self.author}({self.year}), {self.genre}')