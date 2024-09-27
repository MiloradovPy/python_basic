while True:
    numb = input('Введите целое число: ')
    if numb.isdigit():
        numb = int(numb)
        break
    else:
        print('Вы вели не число.')

result = 0

while numb and result != 9:
    tmp = numb % 10
    if tmp > result:
        result = tmp
    numb //= 10

print(result)
