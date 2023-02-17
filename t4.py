# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

inp = input("Input a number: ")

katya = 0
petya = 0
serezha = 0

if inp.isdigit():
    inp = int(inp)
    inp -= round(inp * 33.33/100)
    katya = inp
    petya = (katya / 2) - (katya / 2 / 2)
    serezha = (katya / 2) - (katya / 2 / 2)
    print(f"Катя — {katya}, Петя — {round(petya)}, Серёжа — {round(serezha)}")
else:
    print("Скорее всего не число")