'''
    채용 설명회는 n명의 멘토, 1~k번으로 분류되는 상담유형이 있음
    각 멘토는 k개의 상담 유형 중 하나만 담당할 수 있다.
    (다른 유형의 상담은 불가능하다)
    
    멘토는 동시에 참가자 한 명과 상담 가능하며, 상담 시간은 정확히 참가자가 요청한 시간만큼 걸린다.
    
    다음과 규칙대로 상담을 진행한다.
    - 멘토가 상담 중이 아니면 상담을 시작한다.
    - 유형 담당 멘토가 모두 상담 중이면, 자신의 차례가 올 때까지 기다린다.
      (참가자가 기다린 시간은 참가자가 상담 요청했을 때부터 멘토와 상담을 시작할 때까지의 시간)
    - 모든 멘토는 상담이 끝났을 때 자신의 상담 유형의 상담을 바딕 위해 기다리고 있으면 바로 상담을 진행
      (먼저 상담을 요청한 참가자가 우선된다.)
      
    reqs[a,b,c] = c 유형의 상담을 원하는 참가자가 a 분에 b 분 동안의 상담을 요청했음
    무조건 상담 유형보다 멘토 수가 많음
    
    1. 상담 유형에 따라 멘토 수를 어떻게 분배 할 것인가?
        1) 무조건 유형마다 1명씩은 들어갈 수 있음
        2) 이후, 나머지 인원을 어떤 방식으로 배분하여 최소 기다린 시간을 계산해 낼 것인가?
        
    2. 기다린 시간 계산
'''



import math
from collections import deque
from itertools import permutations, combinations_with_replacement, combinations, product

def calc_wait_time(
    reqs,
    case,
    category_cnt
):
    ret_val = 0
    
    reqs_que = deque(reqs)
    mentors = [deque() for _ in range(category_cnt)] # k개의 카테고리 큐
    while reqs_que:
        cur_req = reqs_que.popleft()
        
        case_idx = cur_req[2] - 1

        # 상담 시간 경과 확인
        for ment in mentors:
            ment_size = len(ment)
            for _ in range(ment_size):
                per = ment.popleft()
                per[1] -= 1
                if per[1] > 0:
                    ment.append(per) # 상담이 아직 끝나지 않음
                else:
                    print(f"상담완료 - 멘토: {ment}, per: {per}\n")
                
        # 멘토 배정
        ment = mentors[case_idx]
        if len(ment) == case[case_idx]:
            # 이미 모두 상담 중
            ret_val += 1
            reqs_que.append(cur_req) # 다시 대기열
            print(f"{cur_req[2]} 멘토 모두 상담 중: {ment}, ret_val: {ret_val}")
            
        else:
            # 상담 가능
            ment.append(cur_req)
            print(f'멘토 배정 - 유형: {cur_req[2]}, {ment}')
            
    return ret_val

def solution(k, n, reqs):
    INF = 1e9
    answer = INF
    
    reqs = [[x[0], x[1], x[2], x[0]+x[1]] for x in reqs] # 상담 끝 추가
    
    # 모든 조합 만들기
    for case in product(range(1, n - k + 2), repeat=k):
        if sum(case) == n:
            wait_time = calc_wait_time(
                reqs,
                case,
                k
            )
            answer = min([answer, wait_time])
    
    return answer



### MAIN ###
if "__main__" == __name__:
    ans_1 = solution(
        3, 5,
        [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]	
    )
    print(ans_1)