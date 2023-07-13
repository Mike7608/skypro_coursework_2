class Player:

    def __init__(self, name: str):
        """
        Инициализация класса
        :param name: Имя пользователя
        """
        self.name = name
        """
        Список использованных слов
        """
        self.list_used_words = list()

    def get_count_used_words(self):
        """
        Возвоащает количнство использованных слов
        """
        return len(self.list_used_words)

    def add_word(self, word):
        """
        Процедура добавляет в список использованных слов новое слово
        :param word: Новое слово
        """
        self.list_used_words.append(word)

    def is_used_current_word(self, word):
        """
        Функция проверяет использовалось ли слово
        :param word: Слово для проверки
        :return: true / false
        """
        return word in self.list_used_words

    def __repr__(self):
        """
        Функция для отображения полей класса
        :return: строка с названиями полей класса и их значениями
        """
        return f"name = {self.name}, list_used_words = {self.list_used_words}"
