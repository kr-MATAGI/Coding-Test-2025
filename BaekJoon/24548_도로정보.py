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
            FPF, PFP, FPF, PFP, FPFPFP
    2)
        계속해서 하나씩 윈도우 옮기면서 누적합을 이용?
    
    3)
        DP
'''

import sys
import copy
from typing import List, Any, Dict
from collections import defaultdict

# 입력
N = int(sys.stdin.readline().strip())
road_infos = list(str(sys.stdin.readline().strip()))

state = (0, 0, 0, 0) # T, G, F, P

freq = defaultdict(int)
freq[state] = 1 # (0,0,0,0) 초기 상태 1

answer = 0
for item in road_infos:
    t, g, f, p = state
    
    if item == 'T':
        t = (t+1) % 3
    elif item == 'G':
        g = (g+1) % 3
    elif item == 'F':
        f = (f+1) % 3
    elif item == 'P':
        p = (p+1) % 3

    state = (t,g,f,p)

    # 이미 같은 상태가 등장했다면, 그 횟수만큼 구간을 만들 수 있음
    answer += freq[state]
    
    # 현재 상태의 등장횟수 증가
    freq[state] += 1

print(answer)
print(freq)

