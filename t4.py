# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Пусть Петя сделал x журавликов,
# тогда Сережа сделал x журавликов,
# а Катя сделала (x + x) * 2 журавликов.
# Все вместе они сделали x + x + (x + x) * 2 = 6x журавликов.
# Отсюда уравнение: 6x = S

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

# s = 0
# pet = 0
# kat = 0
# ser = 0

# pet == ser
# kat == per + ser

# kat = (pet + ser) * 2
# res = s / 6 * 4

# inp = input("Input a number: ")

# katya = 0
# petya = 0
# serezha = 0

# if inp.isdigit():
#     inp = int(inp)
#     inp -= round(inp * 33.33 / 100)
#     katya = inp
#     petya = (katya / 2) - (katya / 2 / 2)
#     serezha = (katya / 2) - (katya / 2 / 2)
#     print(f"Катя — {katya}, Петя — {round(petya)}, Серёжа — {round(serezha)}")
# else:
#     print("Скорее всего не число")