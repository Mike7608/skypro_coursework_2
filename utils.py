import requests
import os
import json
import random
from basic_word import BasicWord


def load_random_word(url, path):
    """
    Функция загружает данные для игры по URL адресу
    если URL не активен или не существует тогда данные
    загружается из локального хранилища,
    выбирает случайное слово для игры и
    создает экземпляр класса `BasicWord`
    :param url: ссылка для загрузки данных
    :param path: путь к локальному файлу
    :return: экземпляр класса `BasicWord`
    """
    # создаем пустую библиотеку для загрузки слова
    words_dict = dict()

    # url запрос на получение данных
    data_url = requests.get(url)

    # если url ресурс данными недоступен, то загружается локальный файл
    if data_url.status_code != 200:

        print(f"URL ссылка '{url}' ошибочна или не актуальна!")
        print("Данные для игры будут загружены из локального хранилища.")

        if os.path.exists(path):
            with open(path, 'r', encoding="utf-8") as file:
                data_file = json.load(file)
            words_dict = data_file.json()
        else:
            print(f"Файл данных '{path}' не найден или не существует!")
            print(f"Приносим свои извинения, но игра на дынный момент не возможна!!!")
    else:
        words_dict = data_url.json()

    # получаем случайный слово для игры из списка
    random_word = random.choice(words_dict)

    # возвращаем экземпляр класса BasicWord
    return BasicWord(random_word["word"], random_word["subwords"])
