'''
    (r,c) 좌표로 나타낼 수 있는 n개의 포인트가 존재한다.

    운송 경로는 총 m개

    사용되는 로봇의 개수는 x개 0초에 동시 출발

    1초마다 r좌표와 c좌표 중 하나가 1만큼 감소하거나 증가한 좌표로 이동할 수 있음 -> 상하좌우

    항상 최단경로로 이동하며, r좌표가 변하는 이동을 c좌표가 이동하는 이동보다 먼저한다. -> 상하 / 좌우

    도착한 로봇은 운송을 마치고 물류 센터를 벗어난다.
    로봇이 물류센터를 벗어나는 경우는 생각하지 않는다.

    같은 좌표에 2대이상 모이면 충돌 위험 상황 -> 몇번 위험 상황이 발생하는가?
'''

from collections import defaultdict


def solution(points, routes):
    answer = 0

    # 포인트 정보를 dict 으로 만듦
    point_info = {i+1: v for i, v in enumerate(points)}
    # print(point_info)

    # 각 초마다 로봇들이 어디에 있었는지
    history = defaultdict(lambda: defaultdict(int))

    for route in routes:
        cur_r, cur_c = point_info[route[0]]
        targets = route[1:]

        # 첫 시작점 넣기
        history[0][(cur_r, cur_c)] += 1
        sec = 1
        for tgt_route in targets:
            tgt_point = point_info[tgt_route]

            # 상,하 부터 움직임
            while cur_r != tgt_point[0]:
                if cur_r < tgt_point[0]:
                    cur_r += 1
                else:
                    cur_r -= 1

                history[sec][(cur_r, cur_c)] += 1
                sec += 1

            # 좌, 우 움직임
            while cur_c != tgt_point[1]:
                if cur_c < tgt_point[1]:
                    cur_c += 1
                else:
                    cur_c -= 1

                history[sec][(cur_r, cur_c)] += 1
                sec += 1

    # 충돌 계산
    for time_step, time_line in history.items():
        # print(f"time_step: {time_step},\ntime_line: {time_line}")
        for coord, cnt in time_line.items():
            if 2 <= cnt:
                answer += 1

    return answer


### MAIN ###
if "__main__" == __name__:
    ans_1 = solution(
        [[3, 2], [6, 4], [4, 7], [1, 4]],
        [[4, 2], [1, 3], [2, 4]]
    )
    print(f"ans_1: {ans_1}\n")

    ans_2 = solution(
        [[3, 2], [6, 4], [4, 7], [1, 4]],
        [[4, 2], [1, 3], [4, 2], [4, 3]]
    )
    print(f"ans_2: {ans_2}\n")

    ans_3 = solution(
        [[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]],
        [[2, 3, 4, 5], [1, 3, 4, 5]]
    )
    print(f"ans_3: {ans_3}\n")