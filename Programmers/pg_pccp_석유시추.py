'''
https://school.programmers.co.kr/learn/courses/30/lessons/250136


세로 길이 n, 가로 길이 m

석유는 덩어리로 나누어 묻혀 있음

나는 시추관을 수직으로 단 하나만 뚫을 떄 가장 많은 석유를 뽑을 수 있는 시추관의 위치를 찾고자 함
시추관은 열 하나를 관통하는 형태여야 하며, 열과 열 사이에 시추관을 뚤을 수 있다.
    0   1  2  3  4  5  6  7
0   [0, 0, 0, 1, 1, 1, 0, 0],
1   [0, 0, 0, 0, 1, 1, 0, 0],
2   [1, 1, 0, 0, 0, 1, 1, 0],
3   [1, 1, 1, 0, 0, 0, 0, 0],
4   [1, 1, 1, 0, 0, 0, 1, 1]
'''

from collections import deque
from typing import List, Tuple

def bfs(
    cur_pos: Tuple[int, int],
    land: List[List[int]],
    visited: List[List[bool]],
):
    score = 0
    que = deque([cur_pos])

    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    def check_in_range(r, c):
        return 0 <= r < len(land) and 0 <= c < len(land[0])

    while que:
        row, col = que.popleft()
        visited[row][col] = True

        if land[row][col] == 0:
            continue

        # 점수 +1 후 사방향 탐색
        score += 1

        for d in range(4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if not check_in_range(next_row, next_col) or visited[next_row][next_col]:
                continue

            visited[next_row][next_col] = True

            if 1 == land[next_row][next_col]:
                que.append((next_row, next_col))
                # print(f"pos: {(row, col)}, score: {score}, visited: {visited[row][col]}, next: {(next_row, next_col)}, que: {que}")
                # input()

    return score

def solution(land):
    answer = 0

    results = [] # 컬럼 인덱스별 뽑은 양 [ 인덱스, 시추 종합 ]

    m_len = len(land)
    n_len = len(land[0])

    # 0 인덱스부터 천천히 뽑아 봅시다
    for c_idx in range(n_len):
        visited = [ [False for _ in range(n_len)] for _ in range(m_len)]
        score = 0
        for r_idx in range(m_len):
            if visited[r_idx][c_idx]:
                continue

            if 0 == land[r_idx][c_idx]:
                continue

            score += bfs(
                cur_pos=(r_idx, c_idx),
                land=land,
                visited=visited
            )

        results.append((c_idx, score))

    results.sort(key=lambda x: x[1], reverse=True)
    answer = results[0][1]
    # print(results)
    return answer


### MAIN ###
if "__main__" == __name__:
    ans_1 = solution([
        [0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 1, 1, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1]
    ])
    print(f"ANS_1: {ans_1}\n")

    ans_2 = solution([
        [1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0],
        [1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1]
    ])
    print(f"ANS_2: {ans_2}\n")
