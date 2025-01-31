from typing import List
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


'''


N, M = map(int, input().split())
field_arr = []
for _ in range(N):
    apple_inp = list(map(int, input().split()))
    field_arr.append(apple_inp)
friends = []
for _ in range(M):
    f_inp = list(map(int, input().split()))
    friends.append(f_inp)

visited = [ [False for _ in range(N)] for _ in range(N) ]
friend_loc = [ [False for _ in range(N)] for _ in range(N) ]

dir_r = [-1, 1, 0, 0] # 상하좌우
dir_c = [0, 0, -1, 1]

max_val = -1

def is_move(
    loc: List[int]
):
    # 격자 안이며, 친구와 겹치지 않음
    return 0 < loc[0] < N and 0 < loc[1] < N and not friend_loc[loc[0]][loc[1]]

def bfs(
    friends_locs: List[List[int]],
    move_count,
    cur_score,
):
    if move_count > 3:
        max_val = cur_score if cur_score > max_val else max_val
        return
    
    for f_loc in friends_locs:
        pass
    
    
bfs(
    friends_locs=friends,
    move_count=0,
    cur_score=0
)

print(max_val)