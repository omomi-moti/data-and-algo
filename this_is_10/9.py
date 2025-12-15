N ,Y = map(int,input().split())
flag = 0 
for A in range(N + 1):
    for B in range(N - A + 1):#ここのプラス１がないと最後の値がAしか更新されない
        C = N - A -B
        if Y == A * 10000 + B * 5000 + C * 1000:
           flag = 1
           break
    if flag == 1:
        break

if Y == A * 10000 + B * 5000 + C * 1000:
    print(A,B,C)

else:
    print(-1,-1,-1)        