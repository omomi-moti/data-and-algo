N = int(input())
D = [int(input()) for _ in range(N)] #この書き方重要
count = 0

while True:
    current_max_moti = max(D)
    current_max_indexs = [i for i,x in enumerate(D) if x == current_max_moti] # この書き方重要
    new_data = [x for i,x in enumerate(D) if i not in current_max_indexs]
    newdata2 = [diff_number for diff_number in range(D) if diff_number != current_max_moti]  
    print(new_data)  
    print(newdata2)  
    count += 1
    D = new_data #ここでDを更新しないと永遠にバグるコードになる
                 #たぶん上の書き方が良くない
    if len(new_data) == 0:
        break

print(count)

