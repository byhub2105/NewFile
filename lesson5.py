# # 1завдання
# a = [1,3,5]
# b = [2,4,6]
# c = []
# c.extend(a)
# c.extend(b)
# c.sort()
# print(c)

# 2 завдання
# words = (input('Введіть речення: '))
# word = words.split()
# count = {}
# for i in word:
#     count = count.get(word)+1
# print(count)

# # 3 завдання 
# lst = ['комп\'ютер','машина','ріг','книга']
# words = []
# for i in lst:
#     if len(i) >4:
#         words.append(i)
# print(words)

# # 4 завдання
# tpl = [(1,2) , (3,4) , (1,2) , (5,6)]
# unique = []
# for i in tpl:
#     if i not in unique:
#         unique.append(i)
# print(unique)

# 5 завдання
items = []
while True:
    item = input('Введіть товар та його ціну у форматі назва:ціна. Щоб завершити напишіть \'завершити\': ')
    if item == 'завершити':
        break
    else:
        items.append(item)
for i in items:
    print(i)