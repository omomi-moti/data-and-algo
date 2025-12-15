N, S = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
# リンゴ・パイナップルをそれぞれ1つずつ購入するとき合計S円になるような買い方が何通りあるか
# ここにプログラムを追記

for i, apple_value in enumerate(A):
    for j,banana_value  in enumerate(B):
        if S == apple_value + banana_value:
            count += 1
        else:
            continue

print(count)

#やっぱり同じ名前はよくない
