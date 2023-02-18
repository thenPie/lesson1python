# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# amt = 0
# try:
#     amt = int(input("Input number "))
# except ValueError:
#     print("Not an integer")
#     quit()

hor = 0
ver = 0
chu_orig = 0
chunks = 0

try:
    hor, ver, chu_orig = int(input("Введите размер шоколадки (горизонтально x вертикально), отломленные дольки k; через Enter: ")), int(input()), int(input())
except (ValueError, TypeError):
    print("Not an integer or not enough values")
    quit()
print()

# print chocolote full size
chunksAmount = 0
print("Chocolate")
i = 0
k = 0
while i < ver:
    while k < hor:
        print(end = "O ")
        k += 1
        chunksAmount += 1
    k = 0
    print()
    i += 1
print(chunksAmount)
print()

chunkRes = 0
how_bigger = 0
chu = hor / chu_orig # is enough room for chu in hor
# print(f"If chu > 1 = enough room for hor, if chu < 1 not enough room in hor; res is {chu}\n")
if chu < 1:          # if not enough room then go here
    chu = chu_orig
    how_bigger = chu_orig - hor
    chu = chu - how_bigger
    # print(f"How bigger is {how_bigger}, chu for hor is {chu}")
    chunks = hor / chu
    if chunks.is_integer():
        # print("chunks is integer")
        if chunks < hor:
            chunkRes = chu
            # print(f"chunkABLE for hor when not enough in hor {chunks}")
    chunks = 0
    chunks = ver / how_bigger
    if chunks.is_integer():
        chunks = int(chunks)
        # print("chunks is integer")
        if chunks < ver:
            chunkRes = chunkRes + chunks
            # print(f"Res is {chunkRes}")
            if chunkRes < chunksAmount:
                print(f"yes {chunkRes} against {chunksAmount}")
        # else:
        #     print("no stop")
    # if chu.is_integer():
    #     how_bigger = chu_orig - hor
    #     print(how_bigger)
    # else:
    #     print(f"Not an integer, chu < 1 not enough room in hor")
elif chu >= 1:       # if enough room in hor for chu then go here
    if chu.is_integer():
        # print("chu is integer")
        chunks = hor / chu_orig
        if chunks.is_integer():
            # print("chunks is integer")
            if chunks < hor:
                # print("chunks < hor")
                # print(f"chunkABLE {chunks}")
                print("yes")
            elif chunks > hor:
                print("chunks > hor")
    else: # useless code, it seems to be
        print("Сколько чего что?")