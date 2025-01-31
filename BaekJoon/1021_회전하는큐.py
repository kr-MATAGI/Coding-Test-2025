import copy
from collections import deque

"""
    N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다.
    이 큐에서 몇 개의 원소를 뽑아내려고 한다.
    지민이는 이 큐에서 다음과 같은 3가지 연산을 할 수 있다.
        1. 첫 번째 원소를 뽑아낸다
        2. 왼쪽으로 한 칸 이동시킨다.
        3. 오른쪽으로 한 칸 이동시킨다.
    
        처음에 포함되어 있던 수 N이 주어진다.
        그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치)
        그 원소를 주어진 순서대로 뽑아내는 데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램
    
    1)
        10  3
        1   2   3
        -> 0

        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        1
        2
        3 -> 2,3번의 연산이 필요가 없다.

    2)
        10  3
        2   9   5
        -> 8

        목표: 2
        1,2,3,4,5,6,7,8,9,10
            왼쪽 최대: 1, 오른쪽 최대 10
            왼쪽으로 진행
        왼: 2,3,4,5,6,7,8,9,10,1
            ->2
            3,4,5,6,7,8,9,10,1
            
        목표; 9
            왼쪽 최대 3, 오른쪽 최대 10
            오른쪽으로 진행
        오:
            1,3,4,5,6,7,8,9,10
        오:
            10,1,3,4,5,6,7,8,9
        오:
            9,10,1,3,4,5,6,7,8

            ->9
            10,1,3,4,5,6,7,8
        
        목표: 5
            왼쪽: 10, 오른쪽 8:
        오:
            8,10,1,3,4,5,6,7
        오:
            7,8,10,1,3,4,5,6
        오:
            6,7,8,10,1,3,4,5
        오:
            5,6,7,8,10,1,3,4

    3)


    왼쪽, 오른쪽으로 움직일지 어떻게 판단하는가?
        1) 하나의 수를 뺄때, 왼쪽 오른쪽 연산 모두 해보고 최소값으로 진행
        2) 양쪽 끝을 확인해본다?
        3) 똑바로 리스트, 거꾸로 리스트 각각 루프에서 매번 돌려본다.
"""

# N: 큐의 크기
# M: 뽑아내려하는 개수
N, M = map(int, input().split())
loc_info = list(map(int, input().split())) # 뽑아 내려고하는 초


answer = 0
n_list = [x for x in range(1, N + 1)]
n_list = deque(n_list)
loc_info = deque(loc_info)
while loc_info:
    cur_target: int = loc_info.popleft()

    step2_move_cnt: int = 0
    step3_move_cnt: int = 0
    
    step_2_copy = copy.deepcopy(n_list)
    step_3_copy = copy.deepcopy(n_list)

    # print('-----')
    while True:
        if step_2_copy[0] == cur_target:
            step_2_copy.popleft()
            answer += step2_move_cnt
            n_list = step_2_copy
            # print(f"->step2: {n_list}, answer: {answer}")
            break
        
        step_2_val: int = step_2_copy.popleft()
        step2_move_cnt += 1
        step_2_copy.append(step_2_val)
        # print(f"cur_target: {cur_target}, step2_val: {step_2_val}, step_2copy: {step_2_copy}")

        if step_3_copy[0] == cur_target:
            step_3_copy.popleft()
            answer += step3_move_cnt
            n_list = step_3_copy
            # print(f"->step3: {n_list}, answer: {answer}")
            break
        step_3_val: int = step_3_copy.pop()
        step3_move_cnt += 1
        step_3_copy.appendleft(step_3_val)
        # print(f"cur_target: {cur_target}, step3_val: {step_3_val}, step_3copy: {step_3_copy}")

print(answer)