import random
from random import shuffle  # импортируем shuffle, чтоб "перемешивать" слово


def shuffle_string(word):
    '''Решил написать себе функцию, которая будет "шафлить" строки, так как random.shuffle строки не шафлит
    :param word: любое строковое значение
    :type word: str
    :return: (str) Возвращает "перемешанную" строку
    '''

    char_list = list(word)
    shuffle(char_list)
    return "".join(char_list)


user_name = input("Введите Ваше имя: ")  # запоминаем имя

points = 0

print("Введите stop для завершения игры\n")  # подсказываем как закончить игру

with open("words.txt", encoding="utf-8") as words:  # открываем файл со словами в режиме чтения
    for line in words:  # перебираем по линиям
        word = line.rstrip()  # забираем линию в переменную, отрезав в конце /n
        shuffled_word = shuffle_string(word) #шафлим функцией

        user_answer = input(f"Угадайте слово: {shuffled_word} \n")

        if user_answer == "stop": #единственная возможность выхода пользователя
            break
        elif user_answer == word: #если угадал
            print("Верно! Вы получаете 10 очков")
            points += 10
        else: #если не угадал
            print(f"Неверно. Верный ответ - {word}")


with open("history.txt", "a", encoding="utf-8") as history:  # дописываем в файл игрок-очки
    history.write(f"\n{user_name}  {points}")


max_points = -1
lines_count = 0
with open("history.txt", encoding="utf-8") as history:  #открываем или создаем history.txt, чтение
    for lines in history:
        lines_count += 1 #счётчик на количество линий (линии = игры)
        name, points = lines.rstrip().split('  ') #распаковываем список на имя\очки
        if int(points) > max_points:
            max_points = int(points) #записываем текущие очки как рекорд, если они больше чем уже записано



print(f"Всего игр сыграно: {lines_count}")
print(f"Максимальный рекорд: {max_points}")



