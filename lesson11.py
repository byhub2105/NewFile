import os
import json
import time
# # 1 завдання
# with open('new_file','w',encoding='utf-8') as new_file:
#     new_file.write(str(input('Введіть подію: ')))
# # 2 завдання
# summary = 0
# with open('marks','w',encoding='utf-8') as marks:
#     for i in range(6):
#         a = str(input('Введіть оцінку: '))
#         marks.write(f'{a}\n')
# with open('marks','r',encoding='utf-8') as marks:
#     lines = marks.readlines()
#     for i in lines:
#         summary+= int(i)
#     average = summary/len(lines)
# print(average)
# # 3 завдання
# if os.path.exists('login_password') == False:
#     login= input('Введіть логін: ')
#     password = input('Введіть пароль: ')
#     with open('login_password','w',encoding='utf-8') as login_password:
#         login_password.write(f'{login}:{password}\n')
# if os.path.exists('login_password'):
#     login= input('Введіть логін: ')
#     password = input('Введіть пароль: ')
#     with open('login_password','a',encoding='utf-8') as login_password:
#         login_password.write(f'{login}:{password}\n')
# # 4 завдання
# if os.path.exists('file'):
#     print('Файл знайдено')
# # 5 завдання
# if os.path.exists('calculator') == False:
#     while True:
#         try:
#             a = int(input('Введи перше число: '))
#             b= int(input('Введи друге число: '))
#         except ValueError:
#             print('Введи число')
#             continue
#         try:
#             operation = int(input('Виберіть операцію\n' \
#         '1 - \'+\'\n' \
#         '2 - \'-\'\n' \
#         '3 - \'*\'\n' \
#         '4 - \'/\'\n' \
#         'Ваш вибір: '))
#         except ValueError:
#             print('Вибери дію')
#             continue
#         if operation == 1:
#             print(f'a+b={a+b}')
#             break
#         elif operation == 2:
#             print(f'a-b={a-b}')
#             break
#         elif operation == 3:
#              print(f'a*b={a*b}')
#              break
#         try:
#             if operation == 4:
#               print(f'a/b={a/b}')
#               break
#         except ZeroDivisionError:
#             print('На нуль ділити не можна')
#             continue
#     with open('calculator','w',encoding='utf-8') as calc:
#         if operation == 1:
#             calc.write(f'{a}+{b}={a+b:.6f}\n')
#         elif operation == 2:
#             calc.write(f'{a}-{b}={a-b:.6f}\n')
#         elif operation == 3:
#             calc.write(f'{a}*{b}={a*b:.4f}\n')
#         elif operation == 4:
#             calc.write(f'{a}/{b}={a/b:.2f}')
# if os.path.exists('calculator') == True:
#     while True:
#         try:
#             a = int(input('Введи перше число: '))
#             b= int(input('Введи друге число: '))
#         except ValueError:
#             print('Введи число')
#             continue
#         try:
#             operation = int(input('Виберіть операцію\n' \
#         '1 - \'+\'\n' \
#         '2 - \'-\'\n' \
#         '3 - \'*\'\n' \
#         '4 - \'/\'\n' \
#         'Ваш вибір: '))
#         except ValueError:
#             print('Вибери дію')
#             continue
#         if operation == 1:
#             print(f'a+b={a+b}')
#             break
#         elif operation == 2:
#             print(f'a-b={a-b}')
#             break
#         elif operation == 3:
#              print(f'a*b={a*b}')
#              break
#         try:
#             if operation == 4:
#               print(f'a/b={a/b}')
#               break
#         except ZeroDivisionError:
#             print('На нуль ділити не можна')
#             continue
#     with open('calculator','a',encoding='utf-8') as calc:
#         if operation == 1:
#             calc.write(f'{a}+{b}={a+b:.6f}\n')
#         elif operation == 2:
#             calc.write(f'{a}-{b}={a-b:.6f}\n')
#         elif operation == 3:
#             calc.write(f'{a}*{b}={a*b:.4f}\n')
#         elif operation == 4:
#             calc.write(f'{a}/{b}={a/b:.2f}\n')
# # 6 завдання
# event = input('Введіть подію: ')
# with open('event','w',encoding='utf-8') as json_event:
#     json.dump(event , json_event , ensure_ascii=False , indent=4)
# with open('event','r',encoding='utf-8') as json_event:
#     file = json.load(json_event)
# print(file)