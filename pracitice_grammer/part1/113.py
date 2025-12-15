def sum_scores(scores):
    return sum(scores)


def output(sum_a, sum_b, sum_c):
    print(sum_a * sum_b * sum_c)
    # ここにプログラムを追記


# -------------------
# ここから先は変更しない
# -------------------


def input_list(N):
    
    l = list(map(int, input().split()))
    return l


# 科目の数 N を受け取る
N = int(input())

# それぞれのテストの点数を受け取る
A = input_list(N)
B = input_list(N)
C = input_list(N)

# それぞれの合計点を計算
sum_A = sum_scores(A)
sum_B = sum_scores(B)
sum_C = sum_scores(C)

# プレゼントの予算を出力
output(sum_A, sum_B, sum_C)
