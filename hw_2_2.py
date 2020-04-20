my_list = []
new_list = []
inter_key = True

# Цикл заполнение списка.
while inter_key:
    my_list.append((input('Введите элемент списка: ')))
    while True:
        next_inp = input('Ввести ещё элемент списка? (Да/Нет)')
        if next_inp.lower() == 'да':
            break
        elif next_inp.lower() == 'нет':
            inter_key = False
            break

list_1 = my_list[::2]  # Cписок из нечётных элементов.
list_2 = my_list[1::2]  # Cписок из чётных элементов.

i = 0
while i <= (len(list_2)-1):
    new_list.append(list_2[i])
    new_list.append(list_1[i])
    i +=1

# Добавляем последний элемент,
# если в исходном списке было нечётное количество элементов.
if len(my_list) % 2 != 0:
    new_list.append((list_1[-1]))

print('\nИсходный список: ',my_list)
print('Отсортированный список: ',new_list)
