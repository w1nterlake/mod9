count_row = int(input("Введите количество рядов: "))
count_seat = int(input("Введите количество сидений в ряде: "))
distance = int(input("Введите расстояние между рядами: "))
for i in range(1, count_row):
    if distance != 0:
        print("="*count_seat, "*"*distance, "="*count_seat)
    else:
        print("="*count_seat)