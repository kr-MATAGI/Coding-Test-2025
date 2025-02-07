import sys
input = sys.stdin.readline

"""
    바이러스가 숙주의 몸속에서 1초당 P배씩 증가한다.

    처음에 바이러스가 K마리가 있었다면, N초 후에는 총 몇 마리의 바이러스로 불어날까?
"""

# 입력
# 바이러스의수, 증가율, 총 시간
K, P, N = map(int, input().strip().split())

# 계산
div_val = 1000000007

cur_val = K
for _ in range(N):
    cur_val *= P
    cur_val %= div_val

print(cur_val)