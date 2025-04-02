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

    for i, item in enumerate(minerals):
        if "diamond" == item:
            minerals[i] = 0
        elif "iron" == item:
            minerals[i] = 1
        else:
            minerals[i] = 2

    #####

    MIN_VAL = float('inf')

    tools = []
    for i, item in enumerate(picks):
        for _ in range(item):
            tools.append(i)

    for case in permutations(tools, len(tools)):
        cur_tired = 0

        tool_que = deque(case)
        cur_tool = tool_que.popleft()
        use_cnt = 5
        for mine in minerals:
            if MIN_VAL <= cur_tired:  # 더 이상 할 필요 없음
                break

            if 0 >= use_cnt:  # 새로운 도구 꺼냄
                if not tool_que:
                    break
                cur_tool = tool_que.popleft()
                use_cnt = 5

            # 곡갱이-광물 피로도 계산
            cur_tired += energe[cur_tool][mine]
            use_cnt -= 1

        if MIN_VAL > cur_tired:
            MIN_VAL = cur_tired

    ###
    answer = MIN_VAL
    return answer