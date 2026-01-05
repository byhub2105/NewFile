print('Plague Inc. Ви - вірус, та повинні заразити весь світ')
plague = ['Бактерія','Вірус','Грибок','Паразит']
countries = ['Китай','США','Індія','Норвегія','Південна Африка']
stats = {
    'infectivity' : 0 ,
    'severity' : 0,
    'lethality': 0
}
transmission = {
    'air' : 0,
    'water' : 0,
    'ground' : 0,
}
transmission_list = ['Повітрям','Землею','Водою']
abilities = {
    'heat_immune' : 0,
    'cold_immune': 0,
}
vaccination = {
    'process' : 0,
    'cured_people' : 0
}
while True:
    print('Виберіть категорію вірусу, за яку ви будете захоплювати світ')
    for i in plague:
        print(i)
    choise = str(input('Ваш вибір: '))
    virus_choise = choise.lower()
    if virus_choise == 'бактерія':
        print('Вітаю! Ви - бактерія. Категорія вірусів яка швидко поширюється, повільно мутує та легко виліковна.')
        stats['infectivity'] = 5
        stats['severity'] = -1
        stats['lethality'] = 2
        break
    elif virus_choise == 'вірус':
        print('Вітаю! Ви - вірус. Категорія вірусів, який швидко поширюється, швидко мутує та яку важко лікувати')
        stats['infectivity'] = 5
        stats['lethality'] = 1
        stats['severity'] = 5
        break
    elif virus_choise == 'грибок':
        print('Вітаю! Ви - грибок. Категорія вірусів, який важко переноситься людьми та повільно поширюється, в більшовсті приводить до летальних випадків')
        stats['infectivity'] = -1
        stats['severity'] = 2
        stats['lethality'] = 5
        break
    elif virus_choise == 'паразит':
        print('Вітаю! Ви - паразит. Категорія вірусів, який помірно поширюється, у залежності від середовища, важко вилікувати')
        stats['infectivity'] = 3
        stats['severity'] = 2
        stats['lethality'] = 5
        break
    else:
        print('Введіть, будь ласка , коректне значення')
while True:
    print('Виберіть країну, у якій ви будете розвиватись')
    for i in countries:
        print(i)
    country = str(input('Ваш вибір: '))
    country_choise = country.lower()
    if country_choise == 'китай':
        print('Ви почали власне захоплення світу в Китаї.Тут різноманітний клімат, проте ви почали в півночі країни, де клімат субтропічний')
        abilities['heat_immune'] = 6
        break
    elif country_choise == 'сша':
        print('Ви почали власне захоплення світу в США. Клімат тут - помірний')
        abilities['cold_immune'] = 5
        abilities['heat_immune'] = 5
        break
    elif country_choise == 'індія':
        print('Ви почали власне захоплення світу у Індії.Клімат тут - тропічний')
        abilities['heat_immune'] = 10
        break
    elif country_choise =='норвегія':
        print('Ви почали власне захоплення світу у Норвегії.Клімат тут - субарктичний')
        abilities['cold_immune'] = 10
        break
    elif country_choise == 'південна африка':
        print('Ви почали власне захоплення світу в Південній Африці. Клімат тут - тропічний')
        abilities['heat_immune'] = 10
        break
print(f'Вітаю! Ви ропочали гру за {virus_choise},ваша початкова місцевість - {country_choise}')
day_count = 0
infected = 1
print('Ваша задача - захопити весь світ своєю хворобою за 20 днів')
while True:
    if vaccination['process'] >= 100:
        break
    elif day_count >= 20:
        break
    start_game = str(input('Щоб розпочати гру, натисніть 1. Щоб завершити, натисніть 2: '))
    if start_game == '2':
        break
    elif start_game == '1':
        while True:
            day_count+=1
            infected*=1.5
            if vaccination['process'] >= 100:
                break
            if day_count >= 20:
                break
            print(f'День:{day_count},кількість захворюваних:{round(infected)}')
            if day_count == 4:       
                while True:
                    print(f'Ви вже заразили {round(infected)}людей. У вас з\'явилась можливість поширюватись іншим способом:')
                    for i in transmission_list:
                        print(i)
                    transmission_choise = str(input('Ваш вибір: '))
                    transmission_choise1 = transmission_choise.lower()
                    if transmission_choise1 =='повітрям' and abilities['cold_immune'] >=7:
                        print('Оскільки ви знаходитесь у місцевості , де холод і мороз, у вас імунітет до низьких температур, тому на землі поширюєтесь швидше. Через це захворіло 1500 людей')
                        stats['infectivity']+=2
                        infected+=1500
                        break
                    elif transmission_choise1 == 'повітрям':
                        print('Ви вибрали спосіб поширення повітрям та успішно заразили 1000 людей')
                        infected+=1000
                        stats['infectivity']+=3
                        transmission['air'] = 2
                        break
                    elif transmission_choise1 == 'землею' :
                        print('Ви вибрали спосіб поширення хвороби - землею. Через це ви успішно заразили 700 людей')
                        infected+=700
                        stats['infectivity']+=2
                        transmission['ground'] = 2
                        break
                    elif transmission_choise1 == 'водою' and abilities['heat_immune'] >= 7:
                        print('Оскільки ви знаходитесь у місцевості , де тропічний клімат, у вас імунітет до високих температур, тому швидше поширюєтесь водою(дощ,річки,озера).Через це захворіло 2000 людей')
                        infected+=2000
                        stats['infectivity']+=3
                        transmission['water']+=2
                        break
                    elif transmission_choise1 == 'водою' :
                        print('Ви вибрали спосіб поширення хвороби - водою. Через це ви успішно заразили 1200 людей')
                        infected+=1200
                        stats['infectivity'] += 1
                        transmission['water'] = 2
                        break
            elif day_count == 8:
                stats['severity']+=2
                print('Ваша хвороба мутувала та тепер її легше знайти у хворих, люди скоро почнуть шукати вакцину')
                if stats['severity'] >6:
                    print('Ви - вірус, тому ви мутуєте більше ніж інші хвороби, вас вже було помічено органами охорони здоров\'я та було почато розробку вакцини')
                    mutation = 0
                    air = 0
                    ground = 0
                    water = 0
                    while True:
                        day_count+=1
                        vaccination['process']+=12
                        infected*=1.5  
                        print(f'Вам терміново потрібно прийняти рішення щодо вакцини.Шкала вакцини -({vaccination["process"]}|100) Ось варіанти\n'
                        '1.Почати мутувати(-20 до прогресу вакцини,доступно тільки 1 раз)\n'
                        '2.Почати поширюватись іншим шляхом(повітрям,водою,землею) \n'
                        '3.Нічого не робити')
                        critical_choise = str(input('Ваш вибір:'))
                        if critical_choise == '1' and mutation == 1 :
                            print('Ви Вже мутували')
                            infected*=1.7
                        elif critical_choise =='1' and mutation == 0 :
                            mutation+=1
                            infected*=1.5
                            print('Ви успішно змутували(-20 до шкали прогресу вакцини)')
                            vaccination['process']-=20
                        elif critical_choise == '2':
                            while True:
                                if vaccination['process'] >=100:
                                    break
                                if day_count >= 20:
                                    break
                                transmission_critical_choise = str(input('Виберіть спосіб поширення:\n'
                                '1.Повітрям\n'
                                '2.Водою\n'
                                '3.Землею\n'
                                'Ваш вибір: '))
                                if transmission_critical_choise == '1' and air ==0:
                                    transmission['air']+=1
                                    air+=1
                                    print('Ви успішно поширились повітрям,заразили 2000 людей та понизили шкалу вакцини на 2')
                                    infected+=2000
                                    vaccination['process']-=2
                                    break
                                elif transmission_critical_choise == '1' and air == 1:
                                    print('Ви вже поширились повітрям')
                                    break
                                elif transmission_critical_choise =='2' and water ==0:
                                    print('Ви успішно поширились водою, заразили 500 людей та понизили шкалу вакцини на 12')
                                    water+=1
                                    infected+=1000
                                    vaccination['process']-=12
                                    break
                                elif transmission_critical_choise =='2' and water ==1:
                                    print('Ви вже поширились водою')
                                    break
                                elif transmission_critical_choise =='3' and ground in range(0,3):
                                    print('Ви успішно поширились землею, заразили 1250 людей та понизили шкалу вакцини на 5')
                                    ground+=1
                                    vaccination['process']-=5
                                    break
                                elif transmission_critical_choise =='3' and ground ==3:
                                    print('Ви вже поширились землею')
                                    break
                        elif critical_choise =='3':
                            print('')
                        if day_count >= 20:
                            print(f'День{day_count}.Шкала вакцини{vaccination["process"]}|Ви заразили весь світ та пройшли гру!Гру завершено')
                            break
                        elif vaccination['process'] >= 100:
                            print(f'День{day_count}.Хворих - {round(infected)}.Люди знайшли вакцину та вилікували всіх хворих! Гру завершено.')
                            break
            elif day_count == 12:
                country_spread_usa_try = 0
                country_spread_south_africa_india_try = 0
                country_spread_norway_try = 0
                country_spread_china_try = 0
                air_transmission = 0
                water_transmission = 0
                ground_transmission = 0
                print('Люди почали шукати вакцину щоб вилікуватись від вашої хвороби(+23 до шкали за один день).')
                while True:
                    day_count+=1
                    infected*=1.7
                    vaccination['process']+=15
                    print(f'День{day_count}.Кількість захворювань {round(infected)} .Шкала знаходження вакцини {vaccination["process"]}|100.')
                    if stats['infectivity']>=7:
                        print('Ваша хвороба швидко поширюється, тому ви додатково заразили 7.000 людей')
                        infected+=7000
                    while True:
                        overall_critical_choise = str(input('Виберіть ваші наступні дії:\n' \
                        '1.Почати поширюватись по інших країнах\n' \
                        '2.Збільшити продуктивність поширення у:повітрі,воді чи землі\n' \
                        '3.Нічого не робити'))
                        if overall_critical_choise == '1' and abilities['cold_immune'] >=7:
                            print('Зараз ви знаходитесь у країні, де клімат субарктичний,тому поки ви не можете поширитись на Індію чи Китай')
                            country_spread_norway = str(input('Виберіть країну, на яку будете поширюватись:\n' \
                            '1.США\n' \
                            '2.Не поширюватись '
                            'Ваш вибір: '))
                            if country_spread_norway == '1' and country_spread_usa_try == 0:
                                print('Ви успішно поширились на США та заразили 10.000 людей, шкала вакцини зменшено на 25')
                                country_spread_usa_try+=1
                                infected+=10000
                                vaccination['process']-=25
                                break
                            elif country_spread_norway == '1' and country_spread_usa_try ==1:
                                print('Ви вже поширились на США')
                                break
                            elif country_spread_norway == '2':
                                print('')
                        elif overall_critical_choise == '1' and abilities['heat_immune']>=7:
                            print('Ви знаходитесь у країні, де клімат тропічний чи субтропічний, тому поки не можете поширюватись на США чи Норвегію')
                            country_spread_south_africa_india = str(input('Виберіть країну , на яку будете поширюватись:\n' \
                            '1.Китай\n' \
                            '2.Не поширюватись'))
                            if country_spread_south_africa_india == '1' and country_spread_south_africa_india_try == 0:
                                country_spread_south_africa_india_try+=1
                                print('Ви успішно поширились на Китай та заразили 20.000 людей, шкала вакцини зменшено на 25')
                                infected+=20000
                                vaccination['process']-=25
                                break
                            elif country_spread_south_africa_india == '1' and country_spread_south_africa_india_try ==1:
                                print('Ви вже поширились на Китай')
                                break
                            elif country_spread_south_africa_india == '2':
                                print('')
                                break
                        elif overall_critical_choise == '1' and abilities['heat_immune'] ==6:
                            print('Ви знаходитесь у Китаї, де клімат переважно субтропічний, тому поки ви не можете поширюватись у США чи Норвегію')
                            country_spread_china = str(input('Виберіть країну, на яку будете поширюватись\n'
                            '1.Індія\n'
                            '2.Південна Африка\n'
                            '3.Не поширюватись\n'
                            'Ваш вибір: '))
                            if country_spread_china == '1' and country_spread_china_try == 0:
                                print('Ви успішно поширились до Індії та заразили 15.000 людей.Шкала вакцини зменшена на 25')
                                infected+=15000
                                vaccination['process']-=25
                                break
                            if country_spread_china == '1' and country_spread_china_try == 1:
                                print('Ви вже поширились на Індію')
                                break
                            if country_spread_china == '2' and country_spread_china_try == 0:
                                print('Ви успішно поширились до Південої Африки та заразили 17.000 людей. Шкала вакцини зменшена на 22')
                                infected+=17000
                                vaccination['process']-=22
                                break
                            if country_spread_china == '2' and country_spread_china_try == 1:
                                print('Ви вже поширились на Південну Африку')
                                break
                        elif overall_critical_choise == '2':
                            print('Виберіть, яким спопсбом будете поширюватись:')
                            transmission_critical_choise1 = str(input('1.Повітрям\n'
                            '2.Водою\n'
                            '3.Землею\n'
                            'Ваш вибір'))
                            if transmission_critical_choise1 == '1' and air_transmission ==0:
                                print('Успішно поширено хворобу повітрям.Ви заразили 12000 людей та шкалу вакцини зменшено на 15')
                                air_transmission+=1
                                infected+=12000
                                vaccination['process']-=15
                            elif transmission_critical_choise1 =='1' and air_transmission ==1:
                                print('Ви вже поширились повітрям')
                                break
                            elif transmission_critical_choise1 =='2' and water_transmission ==0:
                                print('Успішно поширено хворобу водою.Ви заразили 5000 людей та шкалу вакцини зменшено на 20')
                                water_transmission+=1
                                infected+=5000
                                vaccination['process']-=20
                            elif transmission_critical_choise1 == '2' and water_transmission ==0:
                                print('Ви вже поширились водою')
                            elif transmission_critical_choise1 == '3' and ground_transmission ==0:
                                print('Ви успішно поширились землею та заразили 8000 людей. шкала вакцини зменшена на 10')
                                ground_transmission+=1
                                infected+=8000
                                vaccination['process']-=10
                            elif transmission_critical_choise1 == '3' and ground_transmission ==1:
                                print('Ви вже поширились землею')
                                break
                        elif overall_critical_choise == '3':
                            print('Ваша хвороба під загрозою вилікуватись!')
                            break
                    if vaccination['process'] >=100:
                        print('Людство знайшло вакцину та всіх вилікувало! Ви програли')
                        break
                    elif day_count ==20:
                        print(f'День{day_count}, ви заразили весь світ! Гру завершено')
                        break
