N = int(input())
A = list(map(int,input().split()))

flag = 0
count = 0
while flag == 0:

    res = all(v%2 ==0 for v in A)
    if res == True:
        A = [a//2 for a in A]
        #内包表記で書く
        # for i,a in enumerate(A):
        #     A[i] /= 2
        count += 1

    else:
        flag = 1
print(count)