"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""


import heapq
import sys
input = sys.stdin.readline

# 입력
V, E = map(int, input().strip().split()) # 정점, 간선 개수
S = int(input().strip()) # 시작 정점

edges = []
for _ in range(E):
    temp = list(map(int, input().strip().split()))
    edges.append(temp)

# 계산
INF = float('inf')
dist_costs = [ INF for _ in range(V+1) ]
dist_costs[S] = 0

# 그래프 초기 세팅
graph = {v: [] for v in range(V+1)}
for s, e, w in edges:
    graph[s].append(tuple([e, w]))


# (거리, 정점) 형태의 튜플
pri_que = []
heapq.heappush(pri_que, tuple([0, S]))

while pri_que:
    cur_dist, cur_edge = heapq.heappop(pri_que)
    
    # 이미 짧은 경우
    if cur_dist > dist_costs[cur_edge]:
        continue

    # 현재 정점의 인접 정점을 확인해 최단 경로를 갱신
    for neighbor, weight in graph[cur_edge]:
        new_dist = cur_dist + weight
        if new_dist < dist_costs[neighbor]:
            dist_costs[neighbor] = new_dist
            heapq.heappush(pri_que, tuple([new_dist, neighbor]))

# print(graph)
# print(dist_costs)

for ans in dist_costs[1:]:
    if INF != ans:
        print(ans)
    else:
        print('INF')