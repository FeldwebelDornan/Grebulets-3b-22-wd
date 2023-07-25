#Написать программу, которая принимает на вход две строки и выводит их пересечение (т.е. символы, встречающиеся в обеих строках).
def find_same(a,b):
    res = ''
    #удаляем пробелы, потому что нужно найти только общие буквы в строках
    a = a.replace(' ','')
    b = b.replace(' ','')
    #находим большую строку
    max = len(a) if len(a)>len(b) else len(b)
    #проверяем начилие каждой ,буквы в обоих строках, и одновременно
    #проверяем букву на то, что её не добавили в список общих букв
    for i in range(max):
        if a[i] in b and a[i] not in res:
    #добавляем новую букву в строку букв
            res+=a[i]
    return res