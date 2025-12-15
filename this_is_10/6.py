N,A,B = map(int,input().split())

all = 0
count = 0
for i in range(N+1):
    tmp = i
    sum = 0
    while tmp > 0:#この書き方大事だね
        digit = tmp % 10
        sum += digit
        tmp = tmp // 10
        

    if sum >= A and sum <= B:
        count += 1
        all += i

print(all)