from collections import deque
from heapq import heappush, heappop, heapify

'''
    주어진 작업 슬롯 하나로 N개의 자동차를 생산하는 공정을 계획.
    각 i번째 자동차는 생산하기 위해 si단계의 생산 프로세스를 거쳐야한다.

        1) 작업 슬롯의 모든 생산 프로세스들은 자신의 크기만큼 뒤로 움직인다.
            [s_ij-1, s_ij) -> [sij, sij+1)
            - 단 다른 생산프로세스가 차지하는 구간과 겹치게 되면 움직이지 않는다.
            - 슬롯을 통과하여 [0, 1) 밖으로 나온 경우, 이 생산 프로세스는 완료된 것이며, 
            공간을 차지 않는다.

    모든 자동차가 작업 슬롯을 거쳐 생산될 때까지 걸리는 최소시간은 몇 초인가?

    -> softeer 문제 이해가 안됨
    -> 백준가서 보는게 나음 https://www.acmicpc.net/problem/30874    

    # 첫 시도 시간 초과 -> 아마 프로세스 진행하는 부분일 듯
    -> 문제 구조 짤때 무조건 시간복잡도 고려 
        - 특히 2번 루프 도는 거 고려
'''


N = int(input()) # 자동차의 개수
si_list = list(map(int, input().split())) # N개의 생산 프로세스에 대한 각각의 단계수
heap_si = []
for si in si_list:
    heappush(heap_si, si)

answer = 0
min_head = 0
min_val = 0
finish_cnt = 0

while heap_si:
    si_item = heappop(heap_si)

    if 0 == min_val:
        # 초기 추가
        min_val = si_item
    else:
        # 진행 단게에서 추가
        if si_item > min_val:
            min_val = si_item
        # else:
        #     answer += 1

    answer += 1
print(answer + min_val - 1)