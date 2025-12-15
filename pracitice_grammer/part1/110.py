N = int(input())
A = list(map(int,input().split()))#この書き方大事だろうな
sum = 0
ave = 0
çount = 0
for i in A:
    sum += A[çount]
    çount += 1 
ave = sum // N

çount = 0
for i in range(N):
    if A[i] - ave < 0:
        print((A[i] - ave)* -1)
    else:
        print(A[i] - ave)