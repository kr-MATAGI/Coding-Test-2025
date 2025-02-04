'''
    n개로 이루어진 임의의 수열
    이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구한다.
        * 수는 1개 이상 선택해야 한다.
    
    e.g.
        10  -4  3   1   5   6   -35 12  21  -1

        -> 12 + 21 = 33
'''

N_MAX = 100000

# 입력
N = int(input().strip())
num_list = list(map(int, input().strip().split()))

# 계산
DP = [-1001 for _ in range(N)]
DP[0] = num_list[0]

answer = DP[0]
for i in range(1, N):
    DP[i] = max(
        DP[i-1] + num_list[i], num_list[i]
    )

    if DP[i] > answer:
        answer = DP[i]

# print(DP)
print(answer)