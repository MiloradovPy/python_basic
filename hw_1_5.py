while True:
    proс = input('Введите размер выручки: ')
    if proс.isdigit():
        proс = int(proс)
        break
    else:
        print('Вы вели не число.')

while True:
    costs = input('Введите размер издержек: ')
    if costs.isdigit():
        costs = int(costs)
        break
    else:
        print('Вы вели не число.')

if proс > costs:
    print(f"\nВЫ работаете сприбылью.\n"
          f"Рентабельность вашей прибыли: {proс / costs}\n")
    while True:
        empl = input('Введите количество сотрудников: ')
        if empl.isdigit():
            empl = int(empl)
            print(f"Ваша прибыль из расчёта на одного сотрудника: {(proс - costs )/ empl}")
            break
        else:
            print('Вы вели не число.')
elif proс < costs:
    print('\nВы работаете в убыток.')
else:
    print('\nВы работаете в ноль.')