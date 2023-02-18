amt = 0
try:
    amt = int(input("Input number "))
except ValueError:
    print("Not an integer")
    quit()

res = amt / 6
if res.is_integer():
    res = int(res)
    pet = res
    ser = res
    kat = (pet + ser) * 2
    print(f"Катя — {kat}, Петя — {pet}, Серёжа — {ser}")
else:
    print("Cannot be divided into integer")