city = str(input('Em que cidade você nasceu? '))

city = city.strip().title().split()

print('Santo' in city[0])