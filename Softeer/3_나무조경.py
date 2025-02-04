import sys
import copy
from typing import Tuple, List
'''
    우후죽순으로 자라있는 나무들을 정리
    정원은 n * n 격자 모양으로 이루어져 있음, 각 칸에는 하나의 나무가 심어져있음
    
    상하좌우로 맞닿아 있는 경우를 인접한 경우라고 했을 때,
    남우는 최대 4번 인접해 있는 두 나무를 묶으려고 한다.
    이 때 묶은 나무끼리는 서로 겹쳐서는 안되며,
    두 나무가 묶여있을 떄 얻을 수 있는 아름다움은 두 나무의 키의 합
    이 아름다움을 최대로 만들려고 한다.

    * 꼭 4쌍을 고르지 않아도 됨

    * 풀이 방법
        1) 각 좌표에서 마다 4방향 하고, 모든 경우의 수 판단하는 방법

'''

# 입력
N = int(sys.stdin.readline())
tree_arr = []
for _ in range(N):
    row_inp = list(map(int, sys.stdin.readline().split()))
    tree_arr.append(row_inp)

# 계산
dir_r = [-1, 1, 0, 0] # 상하좌우
dir_c = [0, 0, -1, 1]

max_val = -1
visited = [ [False for _ in range(N)] for _ in range(N) ]

def is_valid_pos(i, j):
        if not (0 <= i < N and 0 <= j < N):
            return False
        else:
            if visited[i][j]:
                return False
        
        return True

def bfs(
    cur_pos: Tuple[int, int],
    cur_step: int,
    cur_score: int,
    cur_results: List[Tuple[int, int]]
):
    global max_val, visited, N, tree_arr

    if 8 <= len(cur_results):
        # 최대 4개의 인접 개수를 찾음
        return

    # 현재 위치에 근접한 곳
    for di in range(4):
        near_r = cur_pos[0] + dir_r[di]
        near_c = cur_pos[1] + dir_c[di]

        if not is_valid_pos(near_r, near_c):
            continue
        
        visited[near_r][near_c] = True

        new_score = cur_score
        new_score += tree_arr[near_r][near_c]
        
        new_results = copy.deepcopy(cur_results)
        new_results.append(tuple([near_r, near_c]))

        # 촤대값 갱신
        if new_score > max_val:
            max_val = new_score
            # print(f"""
            # cur_pos:{cur_pos}\n
            # cur_step:{cur_step}\n
            # new_score:{new_score}\n
            # max_score:{max_val}\n
            # new_results:{new_results}\n
            # """)
        
        # 다른 묶음 위치 찾기
        for n_idx in range(N):
            for n_jdx in range(N):
                if not is_valid_pos(n_idx, n_jdx):
                    continue
                
                visited[n_idx][n_jdx] = True

                bfs(
                    cur_pos=tuple([n_idx, n_jdx]),
                    cur_step=cur_step + 1,
                    cur_score=new_score + tree_arr[n_idx][n_jdx],
                    cur_results=new_results + [tuple([n_idx, n_jdx])]
                )

                visited[n_idx][n_jdx] = False
        
        # 원상태
        visited[near_r][near_c] = False

############################################################################################################

for idx in range(N):
    for jdx in range(N):
        start_pos = (idx, jdx)
        
        visited[idx][jdx] = True
        bfs(
            cur_pos=start_pos,
            cur_step=1,
            cur_score=tree_arr[idx][jdx],
            cur_results=[tuple([idx, jdx])]
        )
        visited[idx][jdx] = False

print(max_val)