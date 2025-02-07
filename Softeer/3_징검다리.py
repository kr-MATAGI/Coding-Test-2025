import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
A_list = list(map(int, input().strip().split()))

'''
    3 2 1 4 5
    3 4 5

    1 3 2 4 6 5
    1 3 4 5
'''
# 계산
cur_max_val = A_list[0]
DP = [ 1 for _ in range(N) ]

for i in range(1, N): # 현재 스텝
    for j in range(i): # 이전 스텝 순회
        if A_list[i] > A_list[j]: # 현재 돌 높이가 크다면 이전 기록들을 업데이트
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))
