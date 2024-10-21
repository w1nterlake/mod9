x = 8
y = 10
while True:
    command = input("Введите команду: ")
    if command == 'w':
        if y == 20:
            print("Вы уперлись в северную стену, ваши координаты: ", x, y)
        else:
            y += 1
            print("Ваши координаты: ", x, y)
    elif command == 's':
        if y == 0:
            print("Вы уперлись в южную стену, ваши координаты: ", x, y)
        else:
            y -= 1
            print("Ваши координаты: ", x, y)
    elif command == 'a':
        if x == 0:
            print("Вы уперлись в западнуб стену, ваши координаты:: ", x, y)
        else:
            x -= 1
            print("Ваши координаты: ", x, y)
    elif command == 'd':
        if x == 15:
            print("Вы уперлись в восточную стену, ваши координаты: ", x, y)
        else:
            x += 1
            print("Ваши координаты: ", x, y)
    elif command == 'exit':
        break