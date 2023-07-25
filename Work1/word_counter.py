str = 'казак залез в шалаш'

def wordCounter(str):
    counter = 0
    #записываем в список list каждое слово из строки string
    list = str.split(' ')
    #удаляем от-туда все слова длинной в одну букву
    list = [word for word in list if len(word)>1]
    for word in list:
        #проверяем каждое слово на то что, его первая и последняя буквы одинаковые
        if word[0]==word[len(word)-1]:
            #добавляем 1 в счётчик, если это выполняется
            counter +=1
    return counter
print(wordCounter(str))
