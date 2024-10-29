x = 8
y = 10
while True:
    command = input("Введите команду: ")
    command.lower()
    if command == 'w' and y == 20:
        print("Вы уперлись в северную стену, ваши координаты: ", x, y)
    elif command == 'w' and y < 20:       
        y += 1
        print("Ваши координаты: ", x, y)
    elif command == 's' and y == 0:
        print("Вы уперлись в южную стену, ваши координаты: ", x, y)
    elif command == 's' and y > 0:
        y -= 1
        print("Ваши координаты: ", x, y)
    elif command == 'a' and x == 0:
        print("Вы уперлись в западнуб стену, ваши координаты:: ", x, y)
    elif command == 'a' and x > 0:
        x -= 1
        print("Ваши координаты: ", x, y)
    elif command == 'd' and x == 15:
        print("Вы уперлись в восточную стену, ваши координаты: ", x, y)
    elif command == 'd' and x < 15:
        x += 1
        print("Ваши координаты: ", x, y)
    elif command == 'exit':
        break