try:
    a = int(input('Введите число a:'))
    b = int(input('Введите число b:'))
except Exception:
    print('Введите число')


def diff(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return print('Невозможно выполнить деление на 0')


print(diff(a, b))
