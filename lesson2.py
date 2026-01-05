# 1 завдання
uah = int(input('Введіть суму в UAH: '))
dollar = uah//41.98
euro = uah//48.89
zloty = uah//11.55
print(f'Гривня у доларах {dollar},євро {euro} та злотих {zloty}')
# 2 завдання
num1 = int(input('Введіть перше число: '))
num2 = int(input('Введіть друге число: '))
act = input('Виберіть операцію: +, - , / , * , ** чи √(або впишіть слово "корінь")')
if act == '+':
    print(num1,act,num2 ,'=',num1 + num2)
if act == '-':
    print(num1,act,num2 , '=' ,num1-num2 )
if act == '/':
    print(num1,act,num2 ,'=',num1 / num2)
if act == '*':
    print(num1,act,num2 ,'=',num1 * num2)
if act == '**':
    print(num1,act,num2 ,'=',num1 ** num2)
if act == '√' or act == 'корінь':
    print(num1 , '=' , num1**0.5)
# 3 завдання
word = input('Введіть речення:')
print('Кількість символів:', len(word))
words = word.split()
print('Кількість слів:', len(words))
print(word.upper())
# 4 завдання
year = int(input('Вкажіть рік: '))
if year//4 and year//100 and year > 1582: 
    print('Ваш рік високосний')
else:
    print('Ваш рік не високосний')
# 5 завдання
# numbers = int(input('Введіть ваше число:'))
