month = input('Введите месяц числом:')
type_month = ['лето','осень','зима','весна']
if month == '12' or '1' or '2':
    print(type_month[2])
elif month == '3' or '4' or '5':
    print(type_month[3])
elif month == '6' or '7' or '8':
    print(type_month[0])
elif month == '9' or '10' or '11':
    print(type_month[1])
