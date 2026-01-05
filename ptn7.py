a = {
    'name':'Ярослав',
    'age': 16 ,
    'city':'Львів',
    'position': 'Студент'
}
print(a['name'])
print(a.values())
for key,value in a.items():
    print(f'{key}:{value}')
print(a['fach'])
a['fach']='air engeneer'
print(a['fach'])
print('name' in a)
# # # 
# s={1,2,3,4,5}
# print(s)
# # # 
# a =set('banana')
# b =set('apple')
# print(a)
# print(b)
# print(a&b)
# print(a|b)
# print(a-b)
# print(a^b)
# # # 
# s = {
#     'name':'Chainsaw-man',
#     'year':2025 ,
#     'creator':'Hakita',
# }
# s['genre'] = 'anime'
# for key,value in  s.items():
#     print(f'{key}:{value}')
# 
# s = set(range(1,11))
# s.add(11)
# s.remove(5)
# print(s)
# a = [1,2,3,3,3,4,4,5,6,7,7,7,8,8,9,0, 736]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)