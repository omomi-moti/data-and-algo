N = int(input())
T = list(map(int,input().split()))
min_time = 10000000000
min_number = 0
for i,v in enumerate(T):
    if min_time > v:
        min_time = v
        min_number = i + 1
        
    else:
        continue

print(min_number)

print(T.index(min(T)) + 1)# この書き方の方が強い
