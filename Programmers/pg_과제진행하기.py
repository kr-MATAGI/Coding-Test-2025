'''
    [name, start, playtime]

    새로운 과제가 있다면 해당과제를 시작하고, 진행 중이던것은 멈춤

    진행중이던 과제를 끝냈을 떄, 잠시 멈춰둔 과제가 있다면 멈춰둔 과제를 이어서 진행

    멈춰둔 과제가 여러 개일 경우, 가장 최근에 멈춘 과제부터 시작한다.
'''

from collections import deque
from heapq import heappush, heappop


def solution(plans):
    answer = []

    plan_heap = []
    for plan in plans:
        start = [int(x) for x in plan[1].split(":")]
        start = start[0] * 60 + start[1]

        using = int(plan[-1])
        plan[1] = start
        plan[-1] = using

        heappush(plan_heap, (plan[1], plan))

    #
    wait_que = deque()

    cur_plan = heappop(plan_heap)
    cur_time = cur_plan[0]
    while len(answer) != len(plans):
        if cur_plan and not plan_heap:
            answer.append(cur_plan[1][0])

            if wait_que:
                cur_plan = wait_que.pop()

        # 다음 과목과 차이 계산
        elif plan_heap and (cur_time + cur_plan[1][2] <= plan_heap[0][0]):
            # 다음 과목의 시작시간 이하 -> 다 할 수 있음
            cur_time += cur_plan[1][2]  # 시간 경과
            answer.append(cur_plan[1][0])

            if cur_time < plan_heap[0][0] and wait_que:  # 대기 큐에 있는지 확인
                cur_plan = wait_que.pop()

            else:  # 다음 과목 꺼내옴
                cur_plan = heappop(plan_heap)
                cur_time = cur_plan[0]

        else:
            # 하던 수업 업데이트
            use_time = plan_heap[0][0] - cur_time  # 사용 시간 감소
            cur_plan[1][-1] -= use_time

            # 대기 큐로 전달
            wait_que.append(cur_plan)

            # 새로운 과목 진행
            # print(f"Stop & Start Plan: {cur_plan}, cur_time: {cur_time}, heap.top: {plan_heap[0]}, wait_que: {wait_que}")
            cur_plan = heappop(plan_heap)
            cur_time = cur_plan[0]

    return answer

### MAIN ###
if "__main__" == __name__:
    ans_1 = solution(
        [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
    )
    print(f"ans_1: {ans_1}\n")

    ans_2 = solution(
        [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
    )
    print(f"ans_2: {ans_2}\n")


    ans_3 = solution(
        [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
    )
    print(f"ans_3: {ans_3}\n")