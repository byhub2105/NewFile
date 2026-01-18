import random 
import time
import string as sr 
# # 1 завдання
# try_1 = 0
# final = 3  
# number = random.randint(1,6)
# while True:
#     try :
#         number_guess = int(input('вгадай число:'))
#     except ValueError:
#         print('Введи число!')
#         continue
#     if number_guess == number and try_1 == 1:
#         print('Ти вгадав число з першої спроби!')
#         break
#     elif number_guess == number:
#         print('Ти вгадав число!')
#         break
#     elif final == 1 and try_1 == 2:
#         print('Спроби вичерпано')
#         break
#     elif number_guess != number :
#         final-=1
#         try_1+=1
#         print(f'Не вгадав,ще {final} спроб')
# # 2 завдання
# time_write = int(input('Введіть кількість хвилин для таймеру(хвилини): '))
# time_seconds = time_write*60
# time_wait = time.sleep(time_seconds)
# print(f'Пройшло {time_seconds//60} хвилин')
# # 3 завдання
# while True:
#     try:
#         a = int(input('Секундомір з 3 замірами. Натисніть 1 щоб почати: '))
#         break
#     except ValueError:
#         print('Натисніть 1')
# start_time = time.perf_counter()
# laps = []
# for i in range(1,4):
#     input(f'Натисніть Enter для {i} заміру: ')
#     lap_time = time.perf_counter() - start_time
#     laps.append(lap_time)
#     print(f'Замір {i}, Час: {lap_time:.5f}')
# print('Результати вимірюваннь:\n')
# for i, lap in enumerate(laps , start=1):
#     print(f'Замір {i}, час {lap:.5f}')
# # 4 завдання
# symbols = sr.ascii_letters + sr.digits
# password = ''.join(random.choice(symbols)for i in range(1,9)) 
# print(f'Ось варіант вашого паролю: {password}')
# # 5 завдання
# coin = ['орел','решка']
# while True:
#     try_coin = str(input('Виберіть вашу сторону монети(орел або решка)'))
#     try_coin1 = try_coin.lower()
#     coin_face = random.choice(coin)
#     if try_coin1 == coin_face:
#         print(f'Ви вгадали вашу сторону! Це було {coin_face}')
#         break
#     elif try_coin1 != coin_face:
#         print('Ви не вгадали!')
# # 6 завдання
# str(input('Щоб почати вимірювати, скільки виконується цикл \'for\', натисніть пробіл: '))
# start_time = time.perf_counter()
# for i in range(1,11):
#     print(f'Цикл{i}')
# end_time = time.perf_counter() - start_time
# print(f'Цикл \'for\' виконувався {end_time:.5f} секунд')