# Найдите сумму цифр трехзначного числа.

inp = input("Input three digit number: ")

if inp.isdigit():
    if len(inp) == 3:
        fir = int(inp[0])
        sec = int(inp[1])
        thi = int(inp[2])
        print(f"{fir} + {sec} + {thi} = {fir + sec + thi}")
    else:
        print("Not a three digit number")
else:
    print("Is not an integer")