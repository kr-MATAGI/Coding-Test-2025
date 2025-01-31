import sys
input = sys.stdin.readline

from typing import List
'''
    음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다.
    
        감소하는 수
            321, 950
            0은 0번째 감소하는 수
            1은 1번째 감소하는 수
        아닌 수
            322, 958
        N번째 감소하는 수를 출력하는 프로그램
    
    0,1,2,3,4,5,6,7,8,9,10,20,21,22,30,31,32,33,40,41,42,43,44
    
    1) 18
        1,2,3,4,5,6,7,8,9,
        10,
        20,21,
        30,31,32,
        40,41,42 (18), 43
        ...
        90, 91, 92, 93, 94, 95, 96, 97, 98
        ...
        100 (X)
        ...
        210
        ...
        320, 321,
        310
        ...

    987654
    987653     
'''


'''
    9 8 7 6 5 4
    9 8 7 6 5 3
    9 8 7 6 5 2
    9 8 7 6 5 1
    9 8 7 6 5 0
    9 8 7 6 4 3
    9 8 7 6 4 2
    9 8 7 6 4 1
    9 8 7 6 4 0
    9 8 7 6 3 2
    9 8 7 6 3 1
    9 8 7 6 3 0
    9 8 7 6 2 1
    9 8 7 6 2 0
    9 8 7 6 1 0
    9 8 7 5 4 3
    9 8 7 5 4 2
    9 8 7 5 4 1
    9 8 7 5 4 0
    9 8 7 5 3 2


    9 8 7 2 1 0
    9 8 7 2 1 -1
    9 8 7 2 0 -1
    9 8 7 1 0 -1
'''

answer = -1
inp_item: int = int(input())

now_nums: List[int] = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
limit_nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] # 최소한으로 가져야하는 수

slice_cnt = 0
all_lower_nums = []

while True:
# for _ in range(1000):
    concat_num = int("".join([str(x) for x in now_nums]))    
    all_lower_nums.append(concat_num)
    if 0 == concat_num:
        break
    
    now_nums[-1] -= 1
    if -1 == now_nums[-1]:
        target_i = -1
        for i in range(len(now_nums) - 1, -1, -1):
            now_nums[i] -= 1
            if now_nums[i] >= limit_nums[i+slice_cnt]:
                target_i = i
                break
        
        if target_i == -1:
            target_i = 0
            now_nums = now_nums[:-1]
            slice_cnt += 1
            now_nums[target_i] = 9
            
        
        lower_val = now_nums[target_i]
        for i in range(target_i, len(now_nums)):
            now_nums[i] = lower_val
            lower_val -= 1

# Print
all_lower_nums.reverse()
answer = -1
if inp_item >= len(all_lower_nums):
    print(answer)
else:
    answer = all_lower_nums[inp_item]
    print(answer)

# print('-----\n')
# for item in all_lower_nums:
#     print(item)