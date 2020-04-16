while True:
    time_sec = input('Введите время в секундах: ')
    if time_sec.isdigit():
        time_sec = int(time_sec)
        break
    else:
        print('Вы вели не число.')

print(f"\nВремя в чч:мм:сс - {time_sec // 3600:>02}:{(time_sec % 3600) // 60:>02}:{(time_sec % 3600) % 60:>02}")