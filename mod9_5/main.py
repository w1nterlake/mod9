word = input("Введите слово из 10 букв: ")
mult = 2
sum = 0
for s in word:
    if s == 'b':
        sum += mult
        mult += 2
    elif s == 'a':
        mult += 2
print(sum)