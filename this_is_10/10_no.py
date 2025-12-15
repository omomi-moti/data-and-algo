S = input()

T = S[::-1]

while not len(T) == 0:
    if T[0] == "r":
        if T[3] == "m":
            Tmp = T.removeprefix("remaerd")
            T = Tmp
        elif T[3] == "s":
            Tmp = T.removeprefix("resare")
            T = Tmp
    elif T[0] == "m":
        Tmp = T.removeprefix("maerd")
    elif T[0] == "e":
        Tmp = T.removeprefix("esare")
    else:
        print("NO")
print("YES")





