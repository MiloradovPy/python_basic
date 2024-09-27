while True:
    start = input('Введите количество км которые спортсмен пробегает сейчас: ')
    if start.isdigit():
        start = int(start)
        break
    else:
        print('Вы вели не число.')

while True:
    finish = input('Введите количество км которые спортсмен должен пробегать: ')
    if finish.isdigit():
        finish = int(finish)
        break
    else:
        print('Вы вели не число.')

day = 1
dist = start
while  dist < finish:
    dist *= 1.1
    day += 1

print(f"Вы пробежите {finish} киллометров через {day} дня(ей)")