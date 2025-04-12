'''
https://www.codetree.ai/ko/frequent-problems/problems/magical-forest-exploration/description

마법의 숲 탐색

동, 서, 남쪽은 벽으로 막혀있으며, 정령들은 북쪽을 통해서만 숲으로 들어올 수 있음

총 K명의 정령은 각자 골렘을 타고 숲을 탐색
각 골렘은 십자모양, 중앙을 포함해 총 5칸을 차지함
중앙을 제외한 4칸은 골렘의 탈출구
골렘은 어떤방향에서든 탑승할 수 있지만 내릴 때는 정해진 방향을 통해서만 내리기 가능

골렘은 더 이상 움직이지 못 할 때 까지 다음과 같은 우선순위로 행동한다.

1) 남쪽으로 한 칸
2) 1)의 방법이 안되면 서쪽방향 이동후 반시계방향으로 회전 (출구만 이동)
3) 1)과 2)의 방법이 안되면 동쪽 방향 이동후 시계방향으로 회전

골렘이 모두 이동하고 나면 가장 남쪽으로 이동하는데
골렘의 출구가 다른 골렘의 출구와 이어져있다면 이동
행 번호의 누적을 구해야함

골렘의 몸 일부가 숲을 벗어난 상태라면 새롭게 리셋 시작, 결과도 포함시키지 않음

7 9 6
4 1
5 1
2 1
8 1
2 2
6 0


'''

# Import
import copy
from collections import deque

# Global
MAX_SIZE = 70


# Inputs
R, C, K = map(int, input().split())
'''
    0: 북, 1: 동, 2: 남, 3: 서
    -> 상하좌우 [0, 2, 3, 1]
'''
golems = [] # [골렘이 출발하는 열, 출구 방향 정보]
for _ in range(K):
    c_i, d_i = map(int, input().split())
    golems.append((c_i, d_i))
golem_que = deque(golems)

# Init
'''
    0: 빈 공간
    1: 그냥 골렘
    2: 출구
'''
R += 3
FIELD = [ [0 for _ in range(C)] for _ in range(R) ] # 밖에서 들어오는거 계산
EXIT_POS = [ [False for _ in range(C)] for _ in range(R) ]

class GOLEM:
    def __init__(self, g_id, top, bottom, left, right, mid, ex_d):
        self.g_id = g_id
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.mid = mid

        self.ex_d = ex_d
        self.ex_pos = None
        if 0 == self.ex_d: # 북
            self.ex_pos = self.top
        elif 1 == self.ex_d: # 동
            self.ex_pos = self.right
        elif 2 == self.ex_d: # 남
            self.ex_pos = self.bottom
        elif 3 == self.ex_d: # 서
            self.ex_pos = self.left

    def get_exit_pos(self, reverse:bool=False):
        '''
            북동남서 [0,1,2,3]
            상하좌우 [0,2,3,1]
        '''
        if not reverse:
            self.ex_d += 1
            if 4 == self.ex_d:
                self.ex_d = 0
        else:
            self.ex_d -= 1
            if -1 == self.ex_d:
                self.ex_d = 3

        if 0 == self.ex_d: # 북
            self.ex_pos = self.top
        elif 1 == self.ex_d: # 동
            self.ex_pos = self.right
        elif 2 == self.ex_d: # 남
            self.ex_pos = self.bottom
        elif 3 == self.ex_d: # 서
            self.ex_pos = self.left


    def __str__(self):
        return (f"[{self.g_id}] top: {self.top}, bottom: {self.bottom}, left: {self.left}, right: {self.right}, "
                f"mid: {self.mid}, exit: {self.ex_d}, {self.ex_pos}")

# 함수
def move_golem_down(
    t_golem: GOLEM
):
    next_left = (t_golem.left[0] + 1, t_golem.left[1])
    next_bottom = (t_golem.bottom[0] + 1, t_golem.bottom[1])
    next_right = (t_golem.right[0] + 1, t_golem.right[1])

    if not (
        (0 <= next_left[0] < R and 0 <= next_left[1] < C) and
        (0 <= next_bottom[0] < R and 0 <= next_bottom[1] < C) and
        (0 <= next_right[0] < R and 0 <= next_right[1] < C) and
        (0 == FIELD[next_left[0]][next_left[1]]) and
        (0 == FIELD[next_bottom[0]][next_bottom[1]]) and
        (0 == FIELD[next_right[0]][next_right[1]])
    ):
        return False

    print(f"남쪽 이동: {t_golem}")
    return True


def move_golem_left(t_golem: GOLEM):
    next_top = (t_golem.top[0], t_golem.top[1] - 1)
    next_left = (t_golem.left[0], t_golem.left[1] - 1)
    next_bottom = (t_golem.bottom[0], t_golem.bottom[1] - 1)

    if not (
        (0 <= next_left[0] < R and 0 <= next_left[1] < C) and
        (0 <= next_bottom[0] < R and 0 <= next_bottom[1] < C) and
        (0 <= next_top[0] < R and 0 <= next_top[1] < C) and
        (0 == FIELD[next_left[0]][next_left[1]]) and
        (0 == FIELD[next_bottom[0]][next_bottom[1]]) and
        (0 == FIELD[next_top[0]][next_top[1]])
    ):
        return False

    print(f"서쪽 이동: {t_golem}")
    return True

def move_golem_right(t_golem: GOLEM):
    next_top = (t_golem.top[0], t_golem.top[1] + 1)
    next_right = (t_golem.right[0], t_golem.right[1] + 1)
    next_bottom = (t_golem.bottom[0], t_golem.bottom[1] + 1)

    if not (
        (0 <= next_right[0] < R and 0 <= next_right[1] < C) and
        (0 <= next_bottom[0] < R and 0 <= next_bottom[1] < C) and
        (0 <= next_top[0] < R and 0 <= next_top[1] < C) and
        (0 == FIELD[next_right[0]][next_right[1]]) and
        (0 == FIELD[next_bottom[0]][next_bottom[1]]) and
        (0 == FIELD[next_top[0]][next_top[1]])
    ):
        return False

    print(f"동쪽 이동: {t_golem}")
    return True


# 계산
answer = 0
golem_id = 0
while golem_que:
    c_i, d_i = golem_que.popleft()
    c_i -= 1
    golem_id += 1

    # 1. 시작 위치에 셋팅
    cur_golem = GOLEM(
        g_id=golem_id,
        top=[0, c_i],
        bottom=[2, c_i],
        left=[1, c_i - 1],
        right=[1, c_i + 1],
        mid=[1, c_i],
        ex_d=d_i
    )
    print(f"cur: {cur_golem}")

    # 2. 아래 -> 왼쪽 -> 오른쪽 순으로 움직일 수 있는지 확인
    while True:
        print(f"\n현재 위치: {cur_golem}")

        # 2-1) 아래
        is_able_down = move_golem_down(cur_golem)
        if is_able_down:
            cur_golem.top[0] += 1
            cur_golem.mid[0] += 1
            cur_golem.bottom[0] += 1
            cur_golem.left[0] += 1
            cur_golem.right[0] += 1
            # cur_golem.ex_pos[0] += 1

            continue

        # 2-2) 왼쪽
        is_able_left = move_golem_left(cur_golem)
        if is_able_left:
            temp_golem = copy.deepcopy(cur_golem)
            temp_golem.top[1] -= 1
            temp_golem.mid[1] -= 1
            temp_golem.bottom[1] -= 1
            temp_golem.left[1] -= 1
            temp_golem.right[1] -= 1
            temp_golem.get_exit_pos(reverse=True)

            is_able_left_down = move_golem_down(temp_golem)
            if is_able_left_down:
                cur_golem.top[1] -= 1
                cur_golem.mid[1] -= 1
                cur_golem.bottom[1] -= 1
                cur_golem.left[1] -= 1
                cur_golem.right[1] -= 1
                cur_golem.get_exit_pos(reverse=True)

                cur_golem.top[0] += 1
                cur_golem.mid[0] += 1
                cur_golem.bottom[0] += 1
                cur_golem.left[0] += 1
                cur_golem.right[0] += 1
                # cur_golem.ex_pos[0] += 1

                continue

        # 2-3) 오른쪽
        is_able_right = move_golem_right(cur_golem)
        if is_able_right:
            temp_golem = copy.deepcopy(cur_golem)
            temp_golem.top[1] += 1
            temp_golem.mid[1] += 1
            temp_golem.bottom[1] += 1
            temp_golem.left[1] += 1
            temp_golem.right[1] += 1
            temp_golem.get_exit_pos()

            is_able_right_down = move_golem_down(temp_golem)
            if is_able_right_down:
                cur_golem.top[1] += 1
                cur_golem.mid[1] += 1
                cur_golem.bottom[1] += 1
                cur_golem.left[1] += 1
                cur_golem.right[1] += 1
                cur_golem.get_exit_pos()

                cur_golem.top[0] += 1
                cur_golem.mid[0] += 1
                cur_golem.bottom[0] += 1
                cur_golem.left[0] += 1
                cur_golem.right[0] += 1
                # cur_golem.ex_pos[0] += 1

                continue

            else:
                # 더 이상 이동할 수 없음
                break

        if not is_able_right:
            # 더 이상 이동할 수 없음
            break


    # 3-1 골렘 자리 확정
    print(f"\n골렘 자리: {cur_golem}")
    FIELD[cur_golem.top[0]][cur_golem.top[1]] = cur_golem.g_id
    FIELD[cur_golem.mid[0]][cur_golem.mid[1]] = cur_golem.g_id
    FIELD[cur_golem.left[0]][cur_golem.left[1]] = cur_golem.g_id
    FIELD[cur_golem.right[0]][cur_golem.right[1]] = cur_golem.g_id
    FIELD[cur_golem.bottom[0]][cur_golem.bottom[1]] = cur_golem.g_id

    # 3-2. 출구 위치 표시
    EXIT_POS[cur_golem.ex_pos[0]][cur_golem.ex_pos[1]] = True

    for rrr, eee in zip(FIELD, EXIT_POS):
        print(f"{rrr}\t{eee}")
    print()

    # 4. 삐져나온 부분 있는지 확인
    is_outside = False
    for r_idx in range(0, 3):
        for c_idx in range(C):
            if 0 != FIELD[r_idx][c_idx]:
                is_outside = True
                break
        if is_outside:
            break

    if is_outside:
        # 초기화
        print(f"초기화 - golem_id: {cur_golem.g_id}")
        FIELD = [ [0 for _ in range(C)] for _ in range(R) ]
        EXIT_POS = [ [False for _ in range(C)] for _ in range(R) ]
    else:
        # 5. 남쪽으로 최대 이동
        print(f"남쪽으로 이동 시작 id: {cur_golem.g_id}, {cur_golem.mid}")
        south_pos = cur_golem.mid
        max_value = -float('inf')

        dr = [-1, 1, 0, 0] # 상하좌우
        dc = [0, 0, -1, 1]

        south_que = deque([south_pos])
        visited = [ [False for _ in range(C)] for _ in range(R) ]
        visited[south_pos[0]][south_pos[1]] = True
        while south_que:
            south_golem = south_que.popleft()
            south_id = FIELD[south_golem[0]][south_golem[1]]  # 골렘 아이디

            if max_value < south_golem[0] - 2:
                max_value = south_golem[0] - 2

            for d in range(4):
                next_r = south_golem[0] + dr[d]
                next_c = south_golem[1] + dc[d]

                if 0 <= next_r < 3:
                    # 밖으로 이동할 수 없도록
                    continue

                if not (3 <= next_r < R and 0 <= next_c < C):
                    # 외부로 나갔는가?
                    continue

                if visited[next_r][next_c]:
                    continue
                
                if 0 == FIELD[next_r][next_c]:
                    # 골렘 범위가 아님
                    continue

                if south_id != FIELD[next_r][next_c]:
                    if not EXIT_POS[south_golem[0]][south_golem[1]]:
                        # 만약 두 개의 아이디가 다르다면, 현재 위치는 출구여야 함
                        continue

                print(f"south_golem.cur_pos: {south_golem}, south_id: {south_id}-{FIELD[next_r][next_c]}, {EXIT_POS[south_golem[0]][south_golem[1]]}")
                visited[next_r][next_c] = True
                south_que.append([next_r, next_c])

        # 정답에 누적
        answer += max_value
        print(f"정답에 누적 - [{cur_golem.g_id}]: {max_value}, {answer}")

# 출력
print(answer)