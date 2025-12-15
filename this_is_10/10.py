S = input()
S = S[::-1]

#逆順の書き方
words = ["dreamer","eraser","erase","dream"]
divide = [D[::-1] for D in words]
print(divide)
can = True
i = 0

while i < len(S):
    matched = False
    for d in divide:
        if S[i: i + len(d)] == d:
            matched = True
            i += len(d)
            break
    if not matched:
        can = False
        break
if can:
    print("YES")
else:
    print("NO")