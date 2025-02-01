import copy
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

    예제 샘플은 맞지만 제출시 9개 오답
        -> 즉, 매 시기에 친구들이 정해진 순서로 최댓값을 찾는 동작 방식에 오류가 있을 것
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

# visited = [ [False for _ in range(N)] for _ in range(N) ]
friend_cur_pos = [ [False for _ in range(N)] for _ in range(N) ]

dir_r = [-1, 1, 0, 0] # 상하좌우
dir_c = [0, 0, -1, 1]

max_val = -1

def is_move(
    loc: List[int]
):
    # 격자 안이며, 친구와 겹치지 않음
    return (0 <= loc[0] < N and 0 <= loc[1] < N) and (not friend_cur_pos[loc[0]][loc[1]])

def bfs(
    friends_locs: List[List[int]],
    move_count,
    cur_score,
):
    global max_val

    # 최대 3번만 이동하므로
    if move_count >= 3:
        max_val = cur_score if cur_score > max_val else max_val
        return
    
    # print(f"move_count: {move_count}, cur_score: {cur_score}")
    # for ii in friends_locs:
    #     print(f"{ii}: {field_arr[ii[0]][ii[1]]}")

    next_move_infos: List[int] = []
    for f_loc in friends_locs:
        f_next_dir_idx = -1
        f_next_max_score = -1

        for di in range(4): # 4방향 확인
            # 친구들 마다 움직이게 함
            # 친구들은 같은 시간에 움직임
            # 방향을 탐색하는 조건은 없을까?
            #   - 매번 최대의 선택을 하게 하자

            # 다음 이동하는 곳
            next_r = f_loc[0] + dir_r[di]
            next_c = f_loc[1] + dir_c[di]
            # print(f"{next_r}, {next_c}")
            
            # 움직일 수 있는가?
            if not is_move([next_r, next_c]):
                continue

            # 다음 점수는 몇 점인가?
            next_score = field_arr[next_r][next_c]
            # print(f"{next_r}, {next_c} -> {next_score}")
            if f_next_max_score < next_score:
                f_next_dir_idx = di
                f_next_max_score = next_score
        
        # 다음 이동할 목록 만들기
        if -1 == f_next_dir_idx:
            # 이동 못함
            next_move_infos.append(f_loc)
        else:
            next_r = f_loc[0] + dir_r[f_next_dir_idx]
            next_c = f_loc[1] + dir_c[f_next_dir_idx]
            
            friend_cur_pos[next_r][next_c] = True
            next_move_infos.append([
                next_r,
                next_c,
            ])

    # 다음 단계로 진행
    # 더애지는 스코어
    add_score = sum([field_arr[r][c] for r,c in next_move_infos])
    bfs(
        friends_locs=next_move_infos,
        move_count=move_count+1,
        cur_score=cur_score+add_score
    )

    # 방문 해제
    for mv_info in next_move_infos:
        friend_cur_pos[mv_info[0]][mv_info[1]] = False
    
### MAIN ###
# 현재 친구의 위치는 방문하지 않도록 함
for fr in friends:
    friend_cur_pos[fr[0]][fr[1]] = True

cur_score = sum([field_arr[r][c] for r, c in friends])
bfs(
    friends_locs=friends,
    move_count=0,
    cur_score=cur_score
)

print(max_val)