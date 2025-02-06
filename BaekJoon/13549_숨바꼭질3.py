"""
    수빈이와 동생이 숨바꼭질을 하고 있다.
    수빈이는 0 <= N <= 100,000 에 위치
    동생은 0 <= K <= 100,000

    만약, 수빈이의 위치가 X일 때 
    걷는 다면, 1초 후에 X-1 또는 X+1로 이동하게 된다.
    순산이동을 한다면, 0초 후에 2*X의 위치로 이동하게 된다.


    수빈이가 동생을 가장 빠르게 찾을 수 있는 시

    풀이 방법
    1)
        *2, -1, +1 동작 순서가 관련 있을 것이다.
        *2, +1, -1 순서로 bfs 동작해버리면 계속 커진다.

"""

import sys
from collections import deque
import copy
input = sys.stdin.readline

# 입력
N, K = map(int, input().rstrip().split())
MAX = 100000 * 2

# 계산
INF = float('inf')
dist_costs = [ INF for _ in range(MAX + 1) ]
dist_costs[N] = 0

# Main
positions = deque([N])
while positions:
    cur_pos = positions.popleft()

    # 목적지에 도착
    if cur_pos == K:
        break

    # 점프
    next_pos = cur_pos * 2
    if 0 <= next_pos < MAX and dist_costs[next_pos] > dist_costs[cur_pos]:
        dist_costs[next_pos] = dist_costs[cur_pos]
        positions.appendleft(next_pos)
    
    # 앞으로
    next_pos = cur_pos + 1
    if 0 <= next_pos < MAX and dist_costs[next_pos] > dist_costs[cur_pos] + 1:
        dist_costs[next_pos] = dist_costs[cur_pos] + 1
        positions.append(next_pos)

    # 뒤로
    next_pos = cur_pos - 1
    if 0 <= next_pos < MAX and dist_costs[next_pos] > dist_costs[cur_pos] + 1:
        dist_costs[next_pos] = dist_costs[cur_pos] + 1
        positions.append(next_pos)


# 출력
print(dist_costs[K])
# print(dist_costs[:30])