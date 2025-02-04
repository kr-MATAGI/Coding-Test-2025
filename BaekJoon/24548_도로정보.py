'''
    특정 시내의 도로를 촬영한 데이터를 전달 받았다.
    이 데이터에는 도로 주변의
        나무, 잔디, 울타리, 그리고 사람들을 촬영한 내용이 담겨 있다.

    도로 데이터를 전부 보고 있을 시간이 없어 "흥미로운 구간" 하나를 뽑아서 보려고 한다.

            나무 = T
            잔디 = G
            울타리 = F
            사람 = P

        도로 구간 = 도로의 연속된 일부분 -> 도로의 연속 부분 문자열로 표현됨
        흥미로운 구간 = 길이가 1 이상인 도로 구간 중 그에 속한 모든 물체의 개수가 3의 배수인 것을 의미하낟.

    도로의 정보가 주어졌을 떄, 흥미로운 구간이 될 수 있는 도로 구간의 개수를 구하라

    * 풀이 방법
    1)
        - 윈도우 사이즈 3씩 늘려가며 확인한다.
        - 윈도우가 움직일 때 마다 모든 물체의 개수 확인
            -> 시간 초과 날 거 같은데
                N MAX가 100,000 이므로
                100,000 * 99,999 
        
        FPFPFP
            FPF, PFP, FPF, PFP
    2)
        이분법 활용하면 될 거 같음
'''


import sys
import copy
from typing import List, Any, Dict

# 입력
N = int(sys.stdin.readline().strip())
road_infos = list(str(sys.stdin.readline().strip()))

count_info: Dict[str, int] = {
    "T": 0, # 나무
    "G": 0, # 잔디
    "F": 0, # 울타리
    "P": 0, # 사람
}

# 함수


# 계산
answer = 0

window_size = 3
while window_size <= N:
    for i in range(N):
        if i + window_size > N:
            break
        
        new_count_info = copy.deepcopy(count_info)
        window_slice = road_infos[i:i+window_size]
        # print(window_slice)
        for w in window_slice:
            new_count_info[w] += 1
        # print(new_count_info)

        is_existing = True
        for k, v in new_count_info.items():
            if 0 != v and 0 != v % 3:
                is_existing = False
                break
        
        if is_existing:
            answer += 1

    window_size += 3

# 출력
print(answer)