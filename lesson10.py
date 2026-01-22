import time
import random
# 1 завдання
# while True:
#     try:
#         number = int(input('Напиши число: '))
#         break
#     except ValueError:
#         print('Введи число')
# # 2 завдання
# while True:
#     try:
#         a = int(input('Введи перше число: '))
#         b= int(input('Введи друге число: '))
#     except ValueError:
#         print('Введи число')
#         continue
#     try:
#         operation = int(input('Виберіть операцію\n' \
#         '1 - \'+\'\n' \
#         '2 - \'-\'\n' \
#         '3 - \'*\'\n' \
#         '4 - \'/\'\n' \
#         'Ваш вибір: '))
#     except ValueError:
#             print('Вибери дію')
#             continue
#     if operation == 1:
#         print(f'a+b={a+b}')
#         break
#     if operation == 2:
#          print(f'a-b={a-b}')
#          break
#     if operation == 3:
#          print(f'a*b={a*b}')
#          break
#     try:
#          if operation == 4:
#               print(f'a/b={a/b}')
#               break
#     except ZeroDivisionError:
#          print('На нуль ділити не можна')
#          continue
# # 3 завдання
# try:
#     age = int(input('Введіть ваш вік: '))
#     if age < 1 or age > 120:
#         raise ValueError() 
#     print(f'Ваш вік - {age}')
# except ValueError as ve:
#     print(f'Вік не у діапазоні 1-120 ({age})')
# # 4 завдання
# lst = [1,2,3,4,5]
# while True:
#     try:
#         number = int(input('Введіть індекс списку(0-4): '))
#         print(lst[number])
#         break
#     except IndexError:
#         print('Невірний індекс списку')
#         continue
# # 5 завдання
# while True:
#     try:
#         with open('file.txt','r',encoding='utf-8') as file:
#             data = file.read()
#     except FileNotFoundError:
#         print('Файл не знайдено')
#         break
# # 6 завдання
# uah = 0
# dollar = 0
# euro = 0
# while True:
#     try:
#         choise1 = str(input('Введіть валюту , яку хочете конвертувати(долар,гривня,євро): '))
#         quantity = int(input('Введіть суму: '))
#         choise2 = str(input('Введіть валюту , в яку хочете конвертувати(долар,гривня,євро): '))
#     except ValueError:
#         print('Ввеідть коректне значення')
#         continue
#     if choise1 == 'долар' and choise2 == 'гривня':
#         dollar += quantity
#         uah = dollar*43.15
#         print(f'Долар в гривнях: {uah:.2f}')
#         break
#     elif choise1 == 'долар' and choise2 == 'євро':
#         dollar += quantity
#         euro = dollar*0.85
#         print(f'Долар в євро: {euro}')
#         break
#     elif choise1 == 'гривня' and choise2 == 'долар':
#         uah += quantity
#         dollar = uah/43.15
#         print(f'Гривня в долар: {dollar:.2f}')
#     elif choise1 == 'гривня' and choise2 == 'євро':
#         uah+=quantity
#         euro = uah/50.57
#         print(f'Гривня в євро: {euro:.2f}')
#     elif choise1 == 'євро' and choise2 == 'гривня':
#         euro+=quantity
#         uah= euro*50.57
#         print(f'Євро в гривнях: {uah:.2f}')
#     elif choise1 == 'євро' and choise2 == 'долар':
#         euro+=quantity
#         dollar = euro*1.15
#         print(f'Євро в доларах: {dollar:.2f}')
# 7 завдання 