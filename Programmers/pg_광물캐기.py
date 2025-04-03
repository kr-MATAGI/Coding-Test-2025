'''
    곡갱이: 다이아, 철, 돌 각 0~5개 가지고 있음

    곡갱이-광물 피로도 소모가 다르다.
    광물의 종류에 상관없이 광물을 5개 캐면 더 이상 곡갱이를 사용할 수 없다.

    다음과 같은 규칙을 지킨다
    1) 한 번 사용하면 곡갱이를 끝까지 사용
    2) 광물은 주어진 순서대로만
    3) 모든 광물을 캐거나 더 사용할 곡갱이가 없을 때까지 캔다
'''
from itertools import combinations, product, permutations
from collections import deque

def solution(picks, minerals):
    '''
        picks: [다이아, 철, 돌]
    '''
    answer = 0

    energe = [
        [1, 1, 1],
        [5, 1, 1],
        [25, 5, 1]
    ]

    mine_values = deque([])
    for i, item in enumerate(minerals):
        if "diamond" == item:
            minerals[i] = 0
            mine_values.append(25)
        elif "iron" == item:
            minerals[i] = 1
            mine_values.append(5)
        else:
            minerals[i] = 2
            mine_values.append(1)

    print(mine_values)
    subset_values = []
    add_idx = 0
    while mine_values:
        temp_val = []
        for _ in range(5):
            if not mine_values:
                break
            temp_val.append(mine_values.popleft())
        subset_values.append((add_idx, sum(temp_val)))
        add_idx += 1

    subset_values.sort(key=lambda x: x[1], reverse=True)
    print(subset_values)

    #####
    tool_set = []
    for i in range(3):
        for _ in range(picks[i]):
            tool_set.append(i)
    print(tool_set)

    tool_plan = []
    tool_que = deque(tool_set)
    subset_que = deque(subset_values)
    while tool_que and subset_que:
        sub_item = subset_que.popleft()
        tool_item = tool_que.popleft()

        tool_plan.append((sub_item[0], tool_item))

    tool_plan.sort(key=lambda x: x[0])
    print(tool_plan)

    plan_que = deque(tool_plan)
    cur_plan = plan_que.popleft()
    use_cnt = 5

    for mine in minerals:
        if 0 >= use_cnt:
            if not plan_que:
                break
            cur_plan = plan_que.popleft()
            use_cnt = 5

        answer += energe[cur_plan[1]][mine]

        use_cnt -= 1

    return answer