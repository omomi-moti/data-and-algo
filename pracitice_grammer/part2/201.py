A = list(map(int,input().split()))

for i,x in enumerate(A):
    tmp = x
    if i == 4:
        print("NO")
        break
    elif A[i + 1] == tmp:
        print("YES")
        break
    
#anyってこう使うんだめっちゃ便利じゃん
if any(A[i] == A[i+1] for i in range(len(A)-1)):
    print("YES")
else:
    print("NO")