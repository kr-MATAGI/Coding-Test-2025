"""
    정사각형 모양의 종이가 주어져 있고,
    각 정사각형들은 하얀색 혹은 파란색으로 칠해져 있다.
    주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 종이를 만들려고 한다.

    전체 종이의 크기가 N * N 이라면, 종이를 자르는 규칙은 다음과 같다.
    
        1. 전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로 중간 부분을 잘라서
         N/2 * N/2를 가지는 4개의 색종이로 나눈다.
        
        2. 잘려진 색종이가 모두 하얀색 혹은 파란색으로 이루어질떄까지 반복한다.
    
    입력
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
        

    출력
        하얀색 색종이 개수
        파란색 색종이 개수
"""

import sys
input = sys.stdin.readline

# 입력
N = int(input().rstrip())
n_arr = []
for _ in range(N):
    temp = list(map(int, input().rstrip().split()))
    n_arr.append(temp)


# 계산
answers = [0, 0] # [하얀, 파란]

# 함수
def is_only_one_color(arr):
    if 1 == len(arr):
        # 생종이 한칸
        return True 
    
    base_color = arr[0][0]

    for row in arr:
        for col in row:
            if base_color != col:
                return False
    
    return True

def divide_color_paper(arr):
    global answers

    half_idx = (len(arr) // 2)

    left_up_paper = [] # 좌상
    right_up_paper = [] # 우상
    for idx in range(0, half_idx):
        left_up_paper.append(arr[idx][:half_idx])
        right_up_paper.append(arr[idx][half_idx:])

    left_bottom_paper = [] # 좌하
    right_bottom_paper = [] # 우하
    for idx in range(half_idx, len(arr)):
        left_bottom_paper.append(arr[idx][:half_idx])
        right_bottom_paper.append(arr[idx][half_idx:])

    # print(left_up_paper)
    # print(right_up_paper)
    # print(left_bottom_paper)
    # print(right_bottom_paper)

    for target_paper in [
        left_up_paper, right_up_paper,
        left_bottom_paper, right_bottom_paper
    ]:
        if is_only_one_color(target_paper):
            first_color = target_paper[0][0]
            # print(f"target_paper:\n{target_paper}, first_color: {first_color}\n")
            if 0 == first_color:
                answers[0] += 1 # 하얀
            else:
                answers[1] += 1 # 파란
        else:
            divide_color_paper(target_paper)

# MAIN
if is_only_one_color(n_arr):
    first_color = n_arr[0][0]
    if 0 == first_color:
        answers[0] += 1 # 하얀
    else:
        answers[1] += 1 # 파란
else:
    divide_color_paper(n_arr)

# 출력
print("\n".join([str(x) for x in answers]))

# print(n_arr)