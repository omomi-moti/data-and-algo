A = int(input())
B = int(input())
C = int(input())
X = int(input()) #合計金額

count = 0

for i in range(A+1):
    for j in range(B+1):
        for s in range(C+1):
            if X == 500 * i + 100 * j + 50 * s:
                count += 1

print(count) 


