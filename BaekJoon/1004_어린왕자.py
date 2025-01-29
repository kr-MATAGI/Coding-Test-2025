from typing import List
'''
    https://www.acmicpc.net/problem/1004

    어린왕자의 우주선은
    행성계 간의 이동을 최대한 피해서 여행해야 한다.

    빨간 실선은 어린 왕자가 출발점에서 도착점까지 행성계 진입/이탈 횟수를 최소화하는 경로

    은하수 지도, 출발점, 도착점이 주어졌을 때,
    어린 왕자에게 필요한 최소의 행성계 진입/이탈 횟수를 구하는 프로그램을 작성

    * 행성계의 경계가 맞닿거나 서로 교차한느 경우는 없다.
    * 출발점이나 도착점이 행성계 경계에 걸쳐진 경우 역시 입력으로 주어지지 않는다.

    방법 1.
        - 좌표평면 [0, 2000]에 행성의 차지하는 부분을 모두 표기
        - bfs로 탐색하가면서 진행
        -> 시간 초과 발생할 것 같음
    방법 2.
        - 시작 점 -> 도착점까지 곡선 방정식
        - 해당 직선이 원을 관통하는가 -> 진입/진출 발생
        
'''

T = int(input()) # Test Case
for t_idx in range(T):
    # 전역변수
    MAX_VAL = 1000

    # 입력처리
    start_x, start_y, end_x, end_y = map(int, input().split())
    N = int(input())
    plant_infos: List = []
    for _ in range(N):
        # 중점 x,y, 반지름
        plant_info = list(map(int, input().split()))  
        plant_infos.append(plant_info)

    # 테스트별 계산
    answer = 0
    



    # 테스트 종료
    print(answer)