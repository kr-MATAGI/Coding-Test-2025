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

    targets.sort(key=lambda x: x[1])
    # print(targets)

    prev_tgt = targets[0]
    answer += 1
    for next_tgt in targets[1:]:
        if prev_tgt[0] < next_tgt[0] < prev_tgt[1] or prev_tgt[0] < next_tgt[1] < prev_tgt[1]:
            continue
        elif next_tgt[0] < prev_tgt[0] < next_tgt[1] or next_tgt[0] < prev_tgt[1] < next_tgt[1]:
            continue
        else:
            answer += 1
            prev_tgt = next_tgt

    return answer