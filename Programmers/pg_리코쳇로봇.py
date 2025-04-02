'''
    시작->목표 정확히 멈추기 위해 최소 몇 번의 이동이 필요한가 -> 최단거리

    한번 움직이면 가장자리 혹은 장애물까지 움직인다.
'''
from collections import deque
import math


def solution(board):
    answer = 999999999999

    for i, row in enumerate(board):
        temp = list(row)
        board[i] = temp

    row_len = len(board)
    col_len = len(board[0])

    start_pos = None
    for i in range(row_len):
        for j in range(col_len):
            if 'R' == board[i][j]:
                start_pos = [i, j, 0]
                break
    print(f"start_pos: {start_pos}")

    #
    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]

    pos_que = deque([start_pos])
    visited = [ [False for _ in range(col_len)] for _ in range(row_len)]
    visited[start_pos[0]][start_pos[1]] = True

    while pos_que:
        pos = pos_que.popleft()
        print(f"cur: {pos}, {pos_que}")

        if 'G' == board[pos[0]][pos[1]]:
            if answer > pos[-1]:
                answer = pos[-1]
                break

        for d in range(4):
            next_r = pos[0]
            next_c = pos[1]

            while True:
                if not (0 <= next_r + dr[d] < row_len and 0 <= next_c + dc[d] < col_len):
                    break

                elif board[next_r + dr[d]][next_c + dc[d]] == 'D':
                    break

                next_r += dr[d]
                next_c += dc[d]

            # 장애물 확인
            if not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                pos_que.append([next_r, next_c, pos[-1] + 1])

    return answer if answer != 999999999999 else -1


### MAIN ###
if "__main__" == __name__:
    ans_1 = solution(
        ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
    )
    print(f"ans_1: {ans_1}\n")