# # 1 завдання
# def calc(a,b , operation):
#     if operation =='+':
#         return print(f'{a}+{b}={a+b}')
#     if operation == '-':
#         return print(f'{a}-{b}={a-b}')
#     if operation == '*':
#         return print(f'{a}*{b}={a*b}')
#     if operation == '/':
#         return print(f'{a}/{b}={a//b}')
# print(calc(a=3,b=3,operation='+'))

# # 2 завдання
# last_number = lambda x : abs(x)%10
# print(last_number(213))

# # 3 завдання
# numbers = [1,2,3,4,5]
# quadratic = list(map(lambda x : x**2 , numbers))
# print(quadratic)

# #  4 завдання
# words = ['ліс','ворона','дерево','залізо','дім','вогонь','земля','небо']
# filtered = list(filter(lambda x :len(x) > 5 , words))
# print(filtered)

# #  5 завдання
# students = [
#     {'name':'Ivan', 'age':18},
#     {'name':'Olya','age':20},
#     {'name':'Max','age':17}
# ]
# ascending = list(sorted(students, key=lambda x : x['age']))
# print(ascending)