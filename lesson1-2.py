seconds = int(input('введите время в секундах:'))
mm, ss = divmod(seconds, 60)
hh, mm = divmod(mm, 60)
ret = f"{hh:02d} час" if hh else "00:"
ret += "" if ret else ""
ret += f"{mm:02d}:" if mm else "00:"
ret += "" if ret else ""
ret += f"{ss:02d}"
print(ret)
