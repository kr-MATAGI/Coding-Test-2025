'''
    A 나라가 B 나라를 침공

    미사일을 최소로 사용해서 모든 폭격 미사일을 요격하고자 함

    y축에 걸리는 x좌표에 모든 폭격 미사일을 관통하여 한 번에 요격할 수 있음
    단, (s,e)의 s와 e 지점에서 발사하는 요격 미사일로는 요격할 수 없다.
    요격 미사일은 실수 x 좌표에서도 발사할 수 있다.

    관통, 수평, 개구간, 실수
'''

from collections import deque


def solution(targets):
    answer = 0

    targets = [(i, x[0], x[1], x[1] - x[0]) for i, x in enumerate(targets)]
    targets.sort(key=lambda x: x[-1], reverse=True)
    # print(targets)

    tgt_que = deque(targets)
    del_list = []
    while tgt_que:
        tgt = tgt_que.popleft()
        if tgt[0] in del_list:
            continue
        del_list.append(tgt[0])
        answer += 1

        for i, other in enumerate(targets):
            if i in del_list or tgt[0] == i:
                # 이미 요격되었거나 베이스 대상과 같음
                continue

            if tgt[1] < other[0] < tgt[2] or tgt[1] < other[1] < tgt[2]:
                # print(f"tgt: {tgt}, other: {other}")
                del_list.append(i)

    return answer