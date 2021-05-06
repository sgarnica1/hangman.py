# Reglas:
# 1. Incorpora list comprehensions, manejo de errores y manejo de archivos
# 2.Utiliza el archivo data.txt y léelo para obtener las palabras

# Ayudas y pistas
# 1. Invesgtiga la función enumerate
# El método get de los diccionarios puede servirte
# La sentencia
#   os.system("cls") => Windows
#   os.systen("clear") => Unix
# te serviran para limpiar la pantalla

# Mejora el juego
# 1. Añade un sistema de puntos
# 2. Dibuja al "ahorcado" en cada jugada con código ASCII
# 3. Mejora la interfaz

import random
import re
import os


def read():
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        words = [line for line in f]
        random_word_number = random.randint(0, len(words))
    random_word = words[random_word_number - 1].strip()
    random_word_length = len(random_word)

    normalized_word = random_word.maketrans('áéíóúÁÉÍÓÚ', 'aeiouAEIOU')
    normalized_word = random_word.translate(normalized_word)
    word_dictionary = {count: el for count,
                       el in enumerate(normalized_word.upper())}
    return word_dictionary


def normalize(c):
    c = c.strip()
    c = c.upper()
    normalized_character = c.maketrans('áéíóúÁÉÍÓÚ', 'aeiouAEIOU')
    normalized_character = c.translate(normalized_character)
    return normalized_character


def validate_character(char):
    if re.match("[A-Z]", char):
        return True
    else:
        return False


def clear():
    os.system('cls')


def players_choice(str):
    players_choice_value = normalize(input(str))
    return players_choice_value


def run():
    clear()
    random_word = read()
    default = '_'
    word_to_discover = {i: default for i in range(0, len(random_word))}
    discovered_word = '_ ' * len(random_word)

    counter = 0
    while counter != len(random_word):
        players_choice_value = players_choice('Escoge una letra: ')
        is_letter = validate_character(players_choice_value)

        word = ' '

        while players_choice_value == '' or is_letter == False or len(players_choice_value) > 1:
            word = ''
            for line in word_to_discover.values():
                word = word + line + ' '
            clear()
            print(word + '\n')
            players_choice_value = players_choice('Escoge una letra: ')
            is_letter = validate_character(players_choice_value)

        try:
            if players_choice_value != '':
                for key, c in random_word.items():
                    if c == players_choice_value:
                        if word_to_discover[key] == players_choice_value:
                            continue
                        word_to_discover[key] = players_choice_value
                        counter += 1
            word = ''
            for line in word_to_discover.values():
                word = word + line + ' '
            clear()
            print(word + '\n')

        except:
            print('Error')

        if counter == len(random_word):
            print('¡Ganaste!')
            break


if __name__ == "__main__":
    run()
