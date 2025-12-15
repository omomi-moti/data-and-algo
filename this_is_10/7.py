N = int(input())
A = list(map(int,input().split()))

count = N
Alice_sum = 0
Bob_sum = 0

while count > 0:
    max_val = max(A)
    max_index = A.index(max_val)
    Alice_sum += max_val
    del A[max_index]
    count -= 1
    if count > 0:
         max_val = max(A)
         max_index = A.index(max_val)
         Bob_sum += max_val
         del A[max_index]
         count -= 1
 


print(Alice_sum - Bob_sum)