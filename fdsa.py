hor = 0
ver = 0
chu_orig = 0

try:
    hor, ver, chu_orig = int(input("Введите размер шоколадки (горизонтально x вертикально), отломленные дольки k; через Enter: ")), int(input()), int(input())
except (ValueError, TypeError):
    print("Not an integer or not enough values")
    quit()
print()

chocolate = [[0] * hor] * ver

print(chocolate)

# print chocolote full size
print("Chocolate")
i = 0
k = 0
while i < ver:
    while k < hor:
        print(end = "O ")
        k += 1
    k = 0
    print()
    i += 1
print()

cut = hor - 1

i = 0
while i < hor:
    # print(f"loop {i}")
    # cut = len(chocolate[i]) + cut
    i += 1
print(len(chocolate[0]))
# print(cut)