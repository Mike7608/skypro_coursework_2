import data.constants as CONST
import utils
import players


def main():
    """
    Главная процедура
    """
    # получаем данные для игры
    selected_word = utils.load_random_word(CONST.URL_DATA, CONST.PATH_FILE)

    # просим игрока ввести свое имя
    player_name = input("Введите имя игрока\n")
    if player_name == '' or player_name == ' ':
        player_name = "Аноним :)"

    # создаем экземпляр класс игрока
    player = players.Player(player_name)

    # переменная с количеством возможных слов
    total_words = selected_word.get_count_subwords()
    # случайное слово для игры
    game_word = str(selected_word.word).upper()

    # приветствие игрока
    print(f"Привет, {player.name}!\n"
          f"Составьте {total_words} слов из слова {game_word}\n"
          f"Слова должны быть не короче 3 букв\n"
          f"Чтобы закончить игру, угадайте все слова "
          f"или напишите 'stop'\n"
          f"Поехали!")

    # в цикле запрашиваем ответ у игрока на заданное слово
    # и выводим соответствующую информацию
    while player.get_count_used_words() != selected_word.get_count_subwords():
        # запрос ответа
        user_subword = input(f"Слово '{game_word}', ваше слово: ").strip().lower()

        # проверка ответа
        if len(user_subword) < 3:
            print("Слишком короткое слово!")
        elif user_subword == "stop" or user_subword == "стоп":
            break
        elif player.is_used_current_word(user_subword):
            print("Уже использовано!")
        elif not selected_word.is_correct(user_subword):
            print("НЕВЕРНО!")
        else:
            player.add_word(user_subword)
            # счетчик оставшихся слов
            total_words -= 1

            result = f"ВЕРНО! Осталось угадать еще {total_words} слов."

            if total_words > 0:
                print(result)
            else:
                print(result[0:6])

    # текст завершения игры
    print("=" * 30)
    print(f"Игра завершена, вы угадали {player.get_count_used_words()} слов!")
    print(f"СПАСИБО ЗА ИГРУ, {player_name.upper()}!!!")


# старт программы
if __name__ == '__main__':
    main()