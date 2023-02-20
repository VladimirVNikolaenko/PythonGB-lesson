a = input('Введите целое положительное число:')
b = list(a)
c = 0
for i in b:
    if int(i) > int(c):
        c = i
    else:
        c = c
print(c)
