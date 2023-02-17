# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних
# трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая
# проверяет счастливость билета.

inp = input("Input six digit ticket number: ")

if inp.isdigit():
    if len(inp) == 6:
        fir = int(inp[0])
        sec = int(inp[1])
        thi = int(inp[2])
        fou = int(inp[3])
        fiv = int(inp[4])
        six = int(inp[5])
        if fir + sec + thi == fou + fiv + six:
            print("`Tis a lucky ticket!")
        else:
            print("A regular ticket number")
    else:
        print("Not a six digit number")
else:
    print("Is not an integer")