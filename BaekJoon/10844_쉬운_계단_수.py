'''
    45656이란 수를 보자
    인접한 모든 자리의 차이가 모두 1이다.
    이런 수를 계단 수라고 한다.

    N이 주어질때, 길이가 N인 계단수가 몇 개 있는지 구해보자.
        * 0으로 시작하는 수는 계단 수가 아니다.
'''

MOD_VAL = 1000000000

N = int(input().strip())

DP = [ 0 for _ in range(101) ]

DP[1] = 9
minus_val = 1
for i in range(2, 101):
    DP[i] = (DP[i-1] * 2) - 1
    minus_val += 1

print(DP[N] % MOD_VAL)