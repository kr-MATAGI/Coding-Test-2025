import copy
from collections import deque
from typing import List, Dict, Any
'''
    https://softeer.ai/practice/7727

    m명의 친구를 불러 나무에서 열매를 수확하는 일을 맡김
    나무는 n*n 격자
    각 나무마다 열매 수확가능량이 제한되어 있음

    친구들은 서로 다른 위치에서 출발하여
    1초에 1칸씩 상하좌우 인접한 한 칸으로 움직임
    최종적으로 모든 열매의 수확량을 최대로 만들고자 함

    한 나무에 여러 친구가 방문해도 열매는 딱 한번만 수확가능.
    But, 친구들끼리 한 나무에서 동시에 마주치면 싸움남
    m명의 친구들이 3초동안 최대로 얻을 수 있는 열매 수확량의 총 합을 구하는 프로그램

    예제 샘플은 맞지만 제출시 9개 오답
        -> 즉, 매 시기에 친구들이 정해진 순서로 최댓값을 찾는 동작 방식에 오류가 있을 것

    * 이동 동작
        1) 친구마다 3초안에 이동할 수 있는 모든 경로를 찾는다.
        2) 그 이동경로에서 최대 값을 가지는 순서대로 가지치기를 한다.

        -> 이 방법으로 바꾸고 난뒤 3번 오답, 12번 런타임 에러
'''


N, M = map(int, input().split())
field_arr = []
for _ in range(N):
    apple_inp = list(map(int, input().split()))
    field_arr.append(apple_inp)

friends = []
for _ in range(M):
    f_inp = list(map(int, input().split()))
    f_inp = [x-1 for x in f_inp] # 인덱스화
    friends.append(f_inp)

# 현재 위치 마킹
visited = [ [False for _ in range(N)] for _ in range(N) ]

dir_r = [-1, 1, 0, 0] # 상하좌우
dir_c = [0, 0, -1, 1]

# 친구별 경로리스트
'''
    '친구idx': [
        [score, [x, y], ... ],
        ....
    ]
        
'''
route_infos: Dict[int, List[Any]] = {i: [] for i in range(M)}

# 모든 경로 탐색할 때 사용되는 변수
fi_visited = []

def is_move(x, y):
    return (0 <= x < N and 0 <= y < N) and not fi_visited[x][y]

def dfs(
    idx: int, 
    cur_pos: List[int],
    cur_route: List[int],
    cur_score: int,
    cur_count: int,
):
    if 3 <= cur_count:
        # 현재 경로 저장
        route_infos[idx].append([cur_score, cur_route])
        return

    for di in range(4):
        next_r = cur_pos[0] + dir_r[di]
        next_c = cur_pos[1] + dir_c[di]
        
        if not is_move(next_r, next_c):
            continue
        
        fi_visited[next_r][next_c] = True
        new_route = copy.deepcopy(cur_route)
        new_route.append([next_r, next_c]) 
        dfs(
            idx=idx,
            cur_pos=[next_r, next_c],
            cur_route=new_route,
            cur_score=cur_score + field_arr[next_r][next_c],
            cur_count=cur_count + 1,
        )
        fi_visited[next_r][next_c] = False
    
# 모든 친구들의 경로를 계산
for fi_idx, fi_item in enumerate(friends):
    fi_visited = [ [False for _ in range(N)] for _ in range(N) ]    
    fi_visited[fi_item[0]][fi_item[1]] = True

    dfs(
        idx=fi_idx,
        cur_pos=fi_item,
        cur_route=[fi_item],
        cur_score=field_arr[fi_item[0]][fi_item[1]],
        cur_count=0,
    )

# print(route_infos)

# 경로에서 최고 점수를 찾아냄
'''
4 2
20 26 185 80
100 20 25 80
20 20 88 99
15 32 44 50
1 2
2 3

4 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 2
2 3


처음 친구들의 위치를 표시안해도 될까?
-> 런타임 에러는 아마 Key Error: -1로 생각됨 -> 최적의 경로가 없는 경우
-> 오답은 뭘까>

'''
for ff in friends:
    visited[ff[0]][ff[1]] = True

max_val = 0
fixed_route = []
friend_que = deque([i for i in range(M)])

# for k, v in route_infos.items():
#     print(f"{k}: {v}")

while len(fixed_route) != M:
    cur_max_fdx = -1
    cur_max_score = -1
    cur_max_routs = []
    
    for fidx in range(M):
        if fidx in fixed_route:
            continue

        for route_score, routes in route_infos[fidx]:
            if (route_score > cur_max_score):# or (-1 == cur_max_fdx):
                is_used_route = False
                for route in routes:
                    if route[0] == friends[fidx][0] and route[1] == friends[fidx][1]:
                        continue
                    if visited[route[0]][route[1]]:
                        is_used_route = True
                        break
                if not is_used_route:
                    cur_max_fdx = fidx
                    cur_max_score = route_score
                    cur_max_routes = routes

    # 최선의 경로 확정
    fixed_route.append(cur_max_fdx)
    max_val += cur_max_score
    for r,c in cur_max_routes:
        visited[r][c] = True

print(max_val)