# 1 завдання
steps = 0
day = 0
while True:
    daily_steps = int(input('Скільки ви пройшли кроків за сьогодні: '))
    day+=1
    steps=steps+daily_steps
    if steps >= 100000:
        print('Ви досягнули цілі')
        break
# 2 завдання
num = int(input('Введіть число: ')) 
for i in range(1,11):
    result = num*i 
    print(result)
# 3 завдання
count = 0
while True:
    password = 'dragon'
    password_type = str(input('Впишіть пароль: '))
    if password_type == password:
        print('Вітаю в грі!')
        break
    elif password_type != password :
        print('Спробуйте ще раз')
        count+=1
    if count == 5:
        print('Спробуйте пізніше')
        break
# 4 завдання
a = ('а','е','и','і','о','у')   
# українські голосні
letter = 0
word = str(input('Напишіть слово: '))
for i in word:
    if i in a:
        letter+=1
print('Кількість голосних: ',letter)
# 5 завдання
while True:
    hp = 30
    dmg = int(input('Нанесіть шкоду: '))
    if hp >0:
        hp=hp-dmg
    if hp<0:
        print('Герой повалений!')
        break