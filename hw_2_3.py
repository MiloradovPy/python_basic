while True:
    month_inp = input('Введите номер месяца (1-12): ')
    if month_inp.isdigit():
        month_inp = int(month_inp)
        if month_inp in range(1,13):
            break
        else:
            print('Вы ввели число вне диапазона 1-12.')
    else:
        print('Вы вели не число.')

# Решение через списки.
list_month = [[12,1,2], [3,4,5], [6,7,8], [9,10,11]]

list_seasons = ['Зима', 'Весна', 'Лето', 'Осень']

i=0
while i <= 3:
    if month_inp in list_month[i]:
        print(list_seasons[i])
    i +=1

# Решение через словарь.
dict_seasons = {'Зима': (12,1,2),
                'Весна': (3,4,5),
                'Лето': (6,7,8),
                'Осень': (9, 10, 11)
                }

