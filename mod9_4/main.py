text = input("Введите текст: ")
count = 0
max = 0
for c in text:
    if c != ' ':
        count += 1
        if count > max:
            max = count
    else:
        count = 0

print(max)