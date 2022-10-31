a = input('введите выручку:')
b = input('введите издержки:')
c = int(a) - int(b)
if c > 0:
    print(f'прибыль составила: {c}')
elif c < 0:
    print(f'убыток составил: {c}')
elif c == 0:
    print(f'вы сработали в 0')
