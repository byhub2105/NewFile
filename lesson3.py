# 1 завдання
a = int(input('Введіть число: '))
if a > 0:
    print('Число Додатнє')
elif a < 0:
    print('Число Від\'ємне')
elif a ==0:
    print('Нуль')
# 2 завдання
age = int(input('Вкажіть ваш вік: '))
if age > 0 and age <= 5:
    print('Ви малюк')
elif age > 5 and age <=17:
    print('Ви школяр')
elif age > 17 and age<=23:
    print('Ви студент')
elif age >23 and age <=60:
    print('Ви дорослий')
elif age >=63:
    print('Ви сеньйор')
# 3 завдання
try_count = 0
while True:
    password = str(input('Вкажіть ваш пароль: '))
    if password == 'admin123':
        print('Ви успішно авторизувались')
        break
    else :
        print('Спробуйте ще раз')
        try_count+=1
    if try_count >7:
        print('Спробуйте пізніше')
        break
# 4 завдання 
temperature = float(input('Вкажіть температуру: '))
if temperature < 0:
    print('Мороз')
elif temperature in range(0,20):
    print('Прохолодно')
elif temperature in range(21,30):
    print('Тепло')
elif temperature >30:
    print('Спека')
# 5 завдання
balance = int(input('Баланс грошей: '))
card = str(input('Чи є у вас картка лояльності(так або ні)'))
card_1 = (card.lower())
if balance >= 5000 and card_1 == 'так':
    print('VIP-клієнт')
else :
    print('Звичайний клієнт')
# 6 завдання
number = int(input('Введіть ваше число: '))
while True:
    if number %10 and number %2 ==0:
        print('Число особливе, парне')
        break
    elif number %10 and number %2 !=0:
        print('Число особливе, непарне')
        break
    elif number %2 !=0:
        print('Число непарне')
        break
    elif number %2 ==0:
        print('Число парне')
        break