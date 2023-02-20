a = input('введите стартовую дистанцию пробежки:')
b = input('введите целевую дистанцию:')
a = int(a)
b = int(b)
c = 0
i = 0
while c <= int(b):
    i += 1
    c = a + a*0.1
    print(f'{i}-й день: {a}')
    a = c
print(f'{i+1}-й день: {a}')
