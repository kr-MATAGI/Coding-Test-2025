"""
    N개의 정수 A[1] ~ A[N] 이 주어졌을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성

5
4 1 5 2 3
5
1 3 7 9 5

    * 시간 초과를 어떻게 해결할 것인가?
        - 정렬 후
        - 왼쪽 오른쪽 나눠서 찾기
        - 왼쪽 / 오른쪽 끝의 중간값을 이용해서 찾기
"""

# 전역
import sys
input = sys.stdin.readline

N_MAX = 100000 # 100,000

# 입력
N = int(input().strip())
n_arr = list(map(int, input().strip().split()))

M = int(input().strip())
m_arr = list(map(int, input().strip().split()))

# 계산
n_arr = list(set(n_arr))
n_arr.sort()

for m_item in m_arr:
    left_idx = 0
    right_idx = len(n_arr) - 1
    is_found = False
    
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        mid_val = n_arr[mid_idx]

        if m_item == mid_val:
            is_found = True
            print(1)
            break
        
        elif m_item < mid_val:
            right_idx = mid_idx - 1
        
        else:
            left_idx = mid_idx + 1 

    if not is_found:
        print(0)