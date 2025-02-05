"""
    N * M 크기의 행렬 A와 M * K 행렬 B의 곱을 구하는 프로그램

3 2
1 2
3 4
5 6
2 3
-1 -2 0
0 0 3
"""


# 입력
N, M = map(int, input().split())

A_matrix = []
for _ in range(N):
    temp = list(map(int, input().split()))
    A_matrix.append(temp)

M, K = map(int, input().split())
B_matrix = []
for _ in range(M):
    temp = list(map(int, input().split()))
    B_matrix.append(temp)

# 계산
answers = [ [0 for _ in range(K)] for _ in range(N) ]

for n in range(N):
    row = A_matrix[n]
    for k in range(K):
        col = B_matrix[:]
        col = [x[k] for x in col]
        
        sum_val = 0
        for m in range(M):
            sum_val += row[m] * col[m]
        answers[n][k] = sum_val

# 출력
for ans_row in answers:
    concat = " ".join([str(x) for x in ans_row])
    print(concat)