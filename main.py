
# n, m, k = (int(i) for i in input().split())  # Игра Сапер чтение размеров поля и числа мин
# a = [[0 for j in range(m)] for i in range(n)]
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = -1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] ==0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()


# from random import * # Игра Магический шар
# answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
#            "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
#            "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
#            "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
# print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
# name = input('Как тебя зовут? ')
# print('Привет', name)
# flag = 'да'
# while flag == 'да':
#     question = input('Задайте ваш вопрос магическому шару ')
#     print(f'Итак, ответ на твоой вопрос: "{question}" - {choice(answers)}\n')
#     flag = input('Хочешь еще задать вопрос да/нет: ')
# print("Возвращайся если возникнут вопросы!")


# import random # Генератор паролей
# def generate_password(len_pass, chars):
#     while len_pass > 0:
#         password =''
#         for i in range(len_pass):
#             password += random.choice(chars)
#             len_pass -= 1
#         return print(password)
# digits = '0123456789'
# lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# punctuation = '!#$%&*+-=?@^_'
# symbol = 'il1Lo0O'
# chars = ''
# count_pass = int(input('Введите количество паролей для генерации '))
# len_pass = int(input('Введите необходимую длину пароля '))
# digits_pass = input('включать ли цыфры в пароль да/нет? ')
# lowercase_letters_pass = input('включать ли прописные буквы в пароль да/нет? ')
# uppercase_letters_pass = input('включать ли строчные буквы в пароль да/нет? ')
# punctuation_pass = input('включать ли символы в пароль да/нет? ')
# symbol_pass = input('Исключать ли неоднозначные символы да/нет? ')
# if digits_pass == 'да':
#     chars += digits
# if lowercase_letters_pass == 'да':
#     chars += lowercase_letters
# if uppercase_letters_pass == 'да':
#     chars += uppercase_letters
# if punctuation_pass == 'да':
#     chars += punctuation
# if symbol_pass == 'да':
#     for i in 'il1Lo0O':
#         chars = chars.replace(i, '')
#
# for i in range(count_pass):
#     generate_password(len_pass, chars)


# Шифр Цезаря программа шифруе и дешифрует русские и английские тексты на заданный сдвиг
# alfabet_rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# alfabet_eng = 'abcdefghijklmnopqrstuvwxyz'
# direction = input('Введите необходимое действие: шифрование/дешифрование ' )
# alfabet = input('Введите язык алфавита: русский/английский ')
# step = int(input('Введите кол-во шагов для сдвига '))
# text = input('введите текст для шифрования/дешифрования ')
# if direction == 'шифрование':
#     if alfabet == 'русский':
#         for i in text:
#             if i in " !#$%&'()*+, -./:;<=>?@[\]^_`{|}~":
#                 print(i, end='')
#                 continue
#             if i.isupper():
#                 print(alfabet_rus[(alfabet_rus.find(i.lower()) + step) % len(alfabet_rus)].upper(), end='')
#             else:
#                 print(alfabet_rus[(alfabet_rus.find(i.lower()) + step) % len(alfabet_rus)], end='')
# if direction == 'шифрование':
#     if alfabet == 'английский':
#         for i in text:
#             if i in " !#$%&'()*+, -./:;<=>?@[\]^_`{|}~":
#                 print(i, end='')
#                 continue
#             if i.isupper():
#                 print(alfabet_eng[(alfabet_eng.find(i.lower()) + step) % len(alfabet_eng)].upper(), end='')
#             else:
#                 print(alfabet_eng[(alfabet_eng.find(i.lower()) + step) % len(alfabet_eng)], end='')
# if direction == 'дешифрование':
#     if alfabet == 'русский':
#         for i in text:
#             if i in " !#$%&'()*+, -./:;<=>?@[\]^_`{|}~":
#                 print(i, end='')
#                 continue
#             if i.isupper():
#                 print(alfabet_rus[(alfabet_rus.find(i.lower()) - step) % len(alfabet_rus)].upper(), end='')
#             else:
#                 print(alfabet_rus[(alfabet_rus.find(i.lower()) - step) % len(alfabet_rus)], end='')
# if direction == 'дешифрование':
#     if alfabet == 'английский':
#         for i in text:
#             if i in " !#$%&'()*+, -./:;<=>?@[\]^_`{|}~":
#                 print(i, end='')
#                 continue
#             if i.isupper():
#                 print(alfabet_eng[(alfabet_eng.find(i.lower()) - step) % len(alfabet_eng)].upper(), end='')
#             else:
#                 print(alfabet_eng[(alfabet_eng.find(i.lower()) - step) % len(alfabet_eng)], end='')
# alphabet_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
# s = 'Hawnj pk swhg xabkna ukq nqj.'
# s1 =''
# for k in range(1, 25):
#     for c in s:
#         if c in alphabet_EN:
#             s1 += alphabet_EN[(alphabet_EN.find(c) - k) % 26]
#         elif c in alphabet_en:
#             s1 += alphabet_en[(alphabet_en.find(c) - k) % 26]
#         else:
#             s1 += c
#     print(s1, sep='\n')
#     s1 =''


# alfabet_eng = 'abcdefghijklmnopqrstuvwxyz' # Шифр Цезаря программа шифруе каждое английское слов со сдвигом равным количеству букв в этом слове
# text = input('введите текст ').split()
# print(text[0])
# print(len(text))
# print(sum(c.isalpha() for c in text[0]))
# d = 0
# while d != len(text):
#     for i in text[d]:
#         if i in " !#$%&'()*+, -./:;<=>?@[\]^_`{|}~\"":
#             print(i, end='')
#             continue
#         if i.isupper():
#             print(alfabet_eng[(alfabet_eng.find(i.lower()) + sum(c.isalpha() for c in text[d])) % len(alfabet_eng)].upper(), end='')
#         else:
#             print(alfabet_eng[(alfabet_eng.find(i.lower()) + sum(c.isalpha() for c in text[d])) % len(alfabet_eng)], end='')
#     print(' ', end='')
#     d += 1


# from random import * # Игра Угадайка слов с анимацей))
# world_list = ['рыба', 'карандаш', 'телефон', 'книга', 'комната', 'стол', 'школа', 'машина', 'дерево', 'молоко', 'солнце',
# 'ключ', 'лампа', 'птица', 'кровать', 'зеркало', 'газета', 'чайник', 'мышь', 'печенье', 'носок', 'парашют',
# 'скрипка', 'дракон', 'кошка', 'подушка', 'микрофон', 'буква', 'яблоко', 'стакан', 'яма', 'камень', 'сапог',
# 'батарея', 'трава', 'щетка', 'кино', 'велосипед', 'изумруд', 'свисток', 'джинсы', 'медаль', 'магнитофон',
# 'морковь', 'возможность', 'гитара', 'жалюзи', 'обезьяна', 'старт', 'футбол']

# #функция возвращающая случайное слово из списка
# def get_word():
#     return choice(world_list).upper()
#
# # функция получения текущего состояния
# def display_hangman(tries):
#     stages = [
#         '''
#                            --------
#                            |      |
#                            |      O
#                            |     \\|/
#                            |      |
#                            |     / \\
#                            -
#         ''',
#         '''
#                            --------
#                            |      |
#                            |      O
#                            |     \\|/
#                            |      |
#                            |     /
#                            -
#         ''',
#         '''
#                            --------
#                            |      |
#                            |      O
#                            |     \\|/
#                            |      |
#                            |
#                            -
#         ''',
#         '''
#                            --------
#                            |      |
#                            |      O
#                            |     \\|
#                            |      |
#                            |
#                            -
#         ''',
#         '''
#                            --------
#                            |      |
#                            |      O
#                            |      |
#                            |      |
#                            |
#                            -
#         ''',
#         '''
#                            --------
#                            |      |
#                            |      O
#                            |
#                            |
#                            |
#                            -
#         ''',
#         '''
#                            --------
#                            |      |
#                            |
#                            |
#                            |
#                            |
#                            -
#         ''']
#     return stages[tries]
#
# #Функция осуществляющая основную логику игры
# def play(word):
#     word_completion = [_ for _ in '*' * len(word)]
#     print(word)
#     guessed_letter = [] # Cписок названых букв
#     guessed_words = [] # Список названных слов
#     guessd = False
#     tries = 6
#     print('Давай играть в угадайку русских слов!', '\n', f'У вас есть {tries} попыток', '\n', display_hangman(tries), '\n', *word_completion)
#     while guessd == False:
#         x = input('Назовите букву или слово целиком: ').upper()
#         if x.isalpha() == True and len(x) == 1:
#             if x in guessed_letter:
#                 print('Такую букву уже называли, попробуйте еще раз')
#             if x not in word:
#                 guessed_letter.append(x)
#                 tries -= 1
#                 print('Такой буквы нет', display_hangman(tries))
#             else:
#                 for i in range(len(word_completion)):
#                     if  x == word[i]:
#                         word_completion[i] = x
#                         guessed_letter.append(x)
#                 print(f'Вы угадали букву {x} вот что получилось:', *word_completion)
#         else:
#             if x.isalpha() == False and len(x) == 1:
#                 tries -= 1
#                 print(f'Вы ввели символ не являющийся буквой', display_hangman(tries), '\n',
#                       'Используйте буквы только руского алфавита')
#         if x.isalpha() == True and len(x) == len(word):
#             if x in guessed_words:
#                 print(f'Слово {x} уже называли, попробуйте еще раз')
#             if x != word or len(x) != len(word):
#                 guessed_words.append(x)
#                 tries -= 1
#                 print(f'Ваше слово: {x}, неверное!', display_hangman(tries))
#             else:
#                 if x == word:
#                     print(f'Поздравляем, вы угадали слово {word}! Вы победили!')
#                     break
#         else:
#             if len(x) > 1:
#                 tries -= 1
#                 print(f'Ваше слово: {x}, неверное!', display_hangman(tries), '\n', 'Используйте слова состоящие только из русских букв, равные по длине загаданному!')
#         if tries == 0:
#             guessd = True
#             print(f'Вы исчерпали все свои попытки, поэтому вы повешены! Загаданное слово: {word}')
#         if word == ''.join(word_completion):
#             guessd = True
#             print('Поздравляем, вы угадали слово! Вы победили!')
# play(get_word())
# next_game = input('Хотите сыграть еще раз? Введите да/нет: ')
# while next_game == "да":
#     play(get_word())
# print('Как знаешь, до встречи в следующий раз!')
