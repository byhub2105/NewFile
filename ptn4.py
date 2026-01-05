# counter = 0
# while counter <7:
#     print('Not enough')
#     counter+=1
# if counter == 7:
#     print('Enough')
# for day in range(8):
#     print(f'Day {day}: Hello World!')
# summ = 0
# for i in range(1,50):
#     summ +=i
# print(f'Сума всіх чисел від 1 до 50: {summ}')
# num = 0
# while True:
#     a = int(input('Write number:'))
#     if a > 0 :
#         num+=a
#     elif a == 0:
#         print(f'Summ: {num}')
#         break
# count = 0
# while True:
#     count+=1
#     num_guess = int(input('Chose a number'))
#     if num_guess == 50:
#         print('You have guessed')
#         print('count:', count)
#         break
#     if num_guess < 50:
#         print('The number is bigger')
#     if num_guess > 50:
#         print('The number ist kleiner')
num = 0
for i in range(1,100):
    num+=i
print('Summ:', num)