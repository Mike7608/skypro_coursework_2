class BasicWord:

    def __init__(self, word: str, subwords: list):
        """
        Процедура инициализации BasicWord
        :param word: исходное слово
        :param subwords: набор (список) допустимых подслов
        """
        self.word = word
        self.subwords = subwords

    def is_correct(self, player_word: str):
        """
        Проверка введенного слова в списке допустимых подслов
        :param player_word:
        :return: True / False
        """
        return player_word in self.subwords

    def get_count_subwords(self):
        """
        Подсчет количества подслов
        :return: int значение
        """
        return len(self.subwords)

    def __repr__(self):
        """
        Функция для отображения полей класса
        :return: строка с названиями полей класса и их значениями
        """
        return f"word = {self.word}, subwords = {self.subwords}"
