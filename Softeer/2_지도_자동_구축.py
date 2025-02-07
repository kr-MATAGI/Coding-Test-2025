import sys
input = sys.stdin.readline

"""
    0 - 4
    1 - 9   (16-7)
    2 - 25  (36-11)
    3 - 84? (100-25))

    2   3    5    9
      1    2    4    8
"""

# 입력
N = int(input().strip())

# 계산
cur_val = 2
add_val = 1
point_cnt = 0

for i in range(1, N+1):
    cur_val = cur_val + add_val
    point_cnt = cur_val * cur_val
    add_val *= 2

print(point_cnt)