import copy
from typing import List
'''
    사내 네트워크는 N개의 노드를 가지는 트리 형태의 네트워크
    간선은 N-1개 있어서 모든 노드간의 통신이 가능

    x->y번 노드는 양방향으로 연결되며, 통신에 걸리는 시간은 ti이다.
    Dij는 i와 j노드 사이의 거리를 나타나ㅐ는데, i번에서 j번 노드를 도달하기 위해 걸리는 최소 시간
    (여러 연결을 거침)

    현호는 네트워크 분석을 위해 어떤 노드 i를 기준으로 다른 노드 사이와의 거리 합을 알고 싶다.

'''

N = int(input()) # 노드의 개수

dist_infos = { i: {j: 0 for j in range(1, N+1)} for i in range(1, N+1) }
dir_conn_infos = [ [False for _ in range(N+1)] for _ in range(N+1) ]
for _ in range(N-1):
    x, y, t = map(int, input().split())
    
    dist_infos[x][y] = t
    dist_infos[y][x] = t
    dir_conn_infos[x][y] = True
    dir_conn_infos[y][x] = True
    

# DFS
def dfs(
    target_node: int,
    cur_dist: int,
    cur_routes: List[int]
):
    global dist_infos

    # 노드 거리 정보 업데이트
    if 2 <= len(cur_routes):
        # 처음과 마지막 노드
        first_node = cur_routes[0]
        last_node = cur_routes[-1]
        
        if 0 >= dist_infos[first_node][last_node]:
            dist_infos[first_node][last_node] = cur_dist

            # print(f"target_node: {target_node}, cur_dist: {cur_dist}\ndist_infos[first_node][last_node]: {dist_infos[first_node][last_node]}\ncur_routes:{cur_routes}\n\n")

    # 다음 노드 찾기
    for next_id in range(1, N+1):
        if next_id == target_node:
            # 자기 자신이면 패스
            continue
        elif next_id in cur_routes:
            # Cycle이 안생기게
            continue
        elif not dir_conn_infos[target_node][next_id]:
            # 연결이 없음
            continue
        
        new_routes = copy.deepcopy(cur_routes)
        new_routes.append(next_id)
        dfs(
            target_node=next_id,
            cur_dist=cur_dist + dist_infos[target_node][next_id],
            cur_routes=new_routes,
        )

'''
4
1 2 1
2 3 2
3 4 4

7
1 2 5
1 3 2
1 4 8
3 5 4
3 6 1
4 7 6
'''

# 모든 노드 정보 계산
for node_id in range(1, N+1):
    dfs(
        target_node=node_id,
        cur_dist=0,
        cur_routes=[node_id],
    )

# 노드별 합계 출력
for node_id in range(1, N+1):
    node_score = 0
    for k, v in dist_infos[node_id].items():
        node_score += v
    print(node_score)

# print(dist_infos)