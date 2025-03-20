'''
    같은 시간 대에 게임을 이용하는 사람이 m명 늘어날 때마다 서버 1대가 추가 필요
    어느 시간대의 이용자가 m명 미만이라면 서버 증설이 필요 없음

    어느 시간 대의 이용자가 n*m명 이상 (n+1)*m 명 미만이라면 최소 n대의 서버가 운영되어야 함
    한 번 증설한 서버는 k시간 동안 운영하고 반납
'''

'''
2 ~ 3	3	1	1
10 ~ 11	4	1	1
13 ~ 14	6	2	1
17 ~ 18	13	4	3
23 ~ 24	5	1	1
'''

from collections import deque

def solution(players, m, k):
    answer = 0
    server_list = deque([26]) # 유효시간
    
    # Calc
    for idx, per in enumerate(players):
        # 서버 파기 확인
        for _ in range(len(server_list)):
            serv = server_list.popleft()

            if idx != serv:
                server_list.append(serv)
            # else:
            #     print(f"Del serv - idx: {idx}, serv_size: {len(server_list)} : {server_list}\n")

        # 증설 여부 확인
        able_user_cnt = len(server_list) * m
        if per >= able_user_cnt:
            # 서버 증설
            # add_cnt = ((per - m) // m + 1) - len(server_list) + 1
            add_cnt = per // m - len(server_list) + 1
            answer += add_cnt
            for _ in range(add_cnt):
                server_list.append(idx + k)
            # print(f"{idx}: per: {per}, able: {able_user_cnt}, add_cnt: {add_cnt}, serv_size: {len(server_list)}\n")
    
    return answer


### MAIN ###
if "__main__" == __name__:
    ans_1 = solution(
        [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5],
        3, 5
    )
    print(f"ans_1: {ans_1}\n")


    ans_2 = solution(
        [0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0],
        5,1
    )
    print(f"ans_2: {ans_2}\n")

    ans_3 = solution(
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        1,1
    )
    print(f"ans_3: {ans_3}\n")