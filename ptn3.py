rating = int(input("Введіть оцінку: "))
if rating <= 100 and rating >= 90:
    print('Оцінка: A')
elif rating <= 89 and rating >= 80:
    print('Оцінка: B')
elif rating <=79 and rating >= 70:
    print('Оцінка: C')
elif rating <=69 and rating >=60 and rating >=50:
    print ('Оцінка: F')
elif rating <= 50 and rating >=40:
    print('Оцінка: С')
elif rating == 100:
    print('Дуже добре')
else:
    print('Незадовільно')