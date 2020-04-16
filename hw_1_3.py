while True:
    numb = input('Введите целое число: ')
    if numb.isdigit():
        i = 10 ** len(numb)
        numb = int(numb)
        break
    else:
        print('Вы вели не число.')

count = 1

result = numb

tmp = numb

while count < numb and numb !=1:
    tmp = (tmp * i + numb)
    result += tmp
    count += 1

print('Сумма: ', result)

# while True:
#     numb = input('Введите целое число: ')
#     if numb.isdigit():
#         numb_str = numb
#         numb = int(numb)
#         break
#     else:
#         print('Вы вели не число.')
#
# count = 1
#
# result = numb
#
# tmp = numb_str
#
# while count < numb and numb !=1:
#     tmp = (tmp + numb_str)
#     result = result + int(tmp)
#     count += 1
#
# print('Сумма: ', result)