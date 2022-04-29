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

def file_to_memory(file_name, encoding="utf-8"):
    '''

    :param file_name: имя файла для чтения
    :param encoding: кодировка файла
    :return: (str) Возвращает список со всеми строками из файла
    '''
    with open(file_name, encoding=encoding) as file:
        file_lines = file.readlines()

    return file_lines

def append_str_to_file(file_name, line, encoding="utf-8"):
    '''

    :param file_name: имя открываемого файла
    :param line: строка для добавления
    :param encoding: кодировка в файле
    :return:
    '''

    with open(file_name, "a", encoding=encoding) as file:  # открываем файл в режиме append
        file.write(line)
    return


# основное тело программы
def main():
    user_name = input("Введите Ваше имя: ")  # запоминаем имя

    points = 0 # очки пользователя = 0

    print("Введите stop для завершения игры\n")  # подсказываем как закончить игру

    words_content = file_to_memory("words.txt") #считали файл в память

    for word in words_content:
        origin_word = word.rstrip() #обрезь
        shuffled_word = shuffle_string(origin_word) #перемешали

        user_answer = input(f"Угадайте слово: {shuffled_word} \n") #считали версию

        if user_answer == "stop":  # единственная возможность выхода пользователя
            break
        elif user_answer == origin_word:  # если угадал
            print("Верно! Вы получаете 10 очков")
            points += 10
        else:  # если не угадал
            print(f"Неверно. Верный ответ - {origin_word}")

    append_str_to_file("history.txt", f"\n{user_name}  {points}")# дописываем в файл history инфу игрок-очки

    max_points = -1
    lines_count = 0

    history_content = file_to_memory("history.txt")
    for line in history_content:
        lines_count += 1  # счётчик на количество линий (линии = игры)
        name, points = line.rstrip().split('  ')  # распаковываем список на имя\очки
        if int(points) > max_points:
            max_points = int(points)  # записываем текущие очки как рекорд, если они больше чем уже записано


    print(f"Всего игр сыграно: {lines_count}")
    print(f"Максимальный рекорд: {max_points}")

if __name__ == "__main__":
    main()
