text = input("Введите текст: ")
count = 0
max = 0
for c in text:
    if c != ' ':
        count += 1
    else:
        max = count
        count = 0
print(max)