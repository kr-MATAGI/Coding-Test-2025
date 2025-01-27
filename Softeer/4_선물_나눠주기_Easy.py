import math
'''
    도시는 n개의 마을로 이루어짐
        - 마을은 트리 모양으로 이뤄짐
    각 마을에는 정수 a 값이 주어져 있다.
        0 < a, 해당 마을에 선물이 a개 만큼 놓여 있음
        0 > a, 해당 마을에 선물이 -a개만큼 배달 
    산타는 처음 시작점에 해당하는 마을 s를 잘 골라서 출발한 후
    모든 선물을 배달 완료한 뒤 시작 마을 s로 돌아올려고 한다.
        - 마을을 지날때마다 1초가 소요, 이것이 걸리는 시각을 최소로

    q개의 질의에 대한 답변을 모두 구할려고 한다.
'''

# Inputs
N = int(input())
ai_list = [0] # 기본 값
ai_list.extend(list(map(int, input().split())))

# Dict
v_list = {x: [] for x in range(1, N+1)}
for _ in range(N-1):
    x, y = tuple(map(int, input().split()))
    v_list[x].append(y)
    v_list[y].append(x)

Q = int(input())
q_list = [(1,0,0)] # 기본 탐색
for _ in range(Q):
    q_input = tuple(map(int, input().split()))
    q_list.append(q_input)


# 전역변수
ANSWERS = []

visited = [False for _ in range(N+1)]
visited[0] = True

target_visit_count = 0
for x in ai_list:
    if 0 != x:
        target_visit_count += 1

query_dist_ans = []
is_end_calc = False
rest_items = 0

# 탐색 진행
def dfs(
    start_pos: int,
    cur_pos: int,
    cur_dist: int,
    visit_count: int,
):
    global query_dist_ans, is_end_calc, rest_items
    
    # 선물을 다 나누고 돌아가야 함
    if is_end_calc:
        if cur_pos == start_pos:
            query_dist_ans.append(cur_dist) # 선물 나눠주기 완료
        else:
            can_move_a = v_list[cur_pos]
            for other_a in can_move_a:
                # 방문 중복 검사
                dfs(start_pos, other_a, cur_dist + 1, visit_count) # 이동
        
        return
    
    # 현재 마을의 선물 확인
    a_item = ai_list[cur_pos]
    rest_items += a_item
    
    # 종료 조건
    # 선물이 놓여/배달해야되는 곳 들린 횟수
    if visit_count == target_visit_count:
        is_end_calc = True
        dfs(start_pos, cur_pos, cur_dist + 1, visit_count) # 이동
        return

    # 다른 마을로 이동
    # 이동 가능한 마을 확인
    can_move_a = v_list[cur_pos]
    for other_a in can_move_a:
        if visited[other_a]:
            continue
        
        visited[other_a] = True
        visit_a = ai_list[other_a]
        if 0 != visit_a:
            visit_count += 1

        dfs(start_pos, other_a, cur_dist + 1, visit_count) # 이동
        visited[other_a] = False
        if 0 != visit_a:
            visit_count -= 1


########

for x,y,z in q_list:

    # x에 z 더하고, y에 z를 뺀다
    ai_list[x] += z
    ai_list[y] -= z

    # 최소 거리 계산
    '''
        계산 방법
        1. 각 마을마다 시작지점으로 설정해 loop하여 계산
        2. 모든 선물 배달/획득의 개수 합은 0이다.
        3. 되돌아 가는 경우 외에는 재방문하는 경우는 없다?
    '''
    min_dist = math.inf
    for start_pos in range(1, N+1):
        if 0 > ai_list[start_pos]:
            # 처음부터 선물을 줘야한다면 pass
            continue

         # 초기화 작업
        rest_items = 0
        is_end_calc = False
        query_dist_ans = []

        visited[start_pos] = True
        visit_a = ai_list [start_pos]
        visit_count = 0
        if 0 != visit_a:
            visit_count += 1

        dfs(start_pos, start_pos, 0, visit_count)
        visited[start_pos] = False

        min_dist = min(query_dist_ans)
    
    ANSWERS.append(min_dist)
    
    # 쿼리 끝나면 다시 복구
    ai_list[x] -= z
    ai_list[y] += z