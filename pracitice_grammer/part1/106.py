A,sign,B =input().split()
A = int(A)
B = int(B)

if sign == "?" or sign == "!" or sign == "=":
    print("error")
elif sign == "+":
    print(A + B)
elif sign == "-":
    print(A - B)
elif sign == "*":
    print(A * B)
elif sign == "/":
     if B == 0:
         print("error")
     else:
         print(A // B)

