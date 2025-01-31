import math
import copy
"""
    N행 M열의 표가 있고, 각 칸에는 숫자가 하나씩 적혀있다.
    연두는 서로 다른 1개 이상의 칸을 선택하려고 하는데,
        1) 행의 번호가 선택한 순서대로 등차수열을 이루고 있어야 하고
        2) 열의 번호도 선택한 순서대로 등차수열을 이루고 있어야 한다.
        3) 이렇게 선택한 칸에 적힌 수를 순서대로 이어붙이면 정수를 하나 만들 수 있다.
    연두가 만들 수 있는 정수 중에서 가장 큰 완전 제곱수를 구해보자
    * 완전제곱수 : 어떤 정수를 제곱한 수

    1)
        2   3
        1   2   3
        4   5   6

        (0,0) -> (1,1) : 15
        (0,0) -> (1,2) : 16

        (0,1) -> (1,2) : 26

        (1,1) -> (0,0) : 51
        
        (1,2) -> (0,1) : 62
        (1,2) -> (0,0) : 61

        12, 23, 13, 45, 56, 46
        21, 32, 31, 54, 65, 64
        123, 321, 456, 654

        1   2   3   1   2   3   1   2   3
        1   2   3   2   1   3
        4   5   6

"""


def is_full_num(num: int):
    # return math.sqrt(num).is_integer()
    res = int(math.sqrt(num))
    # print(res)
    # print(res * res)
    return res * res == num

# (행, 열)
N, M = map(int, input().split())
inp_items = []
for _ in range(N):
    temp_inp = str(input())
    temp_inp = list(temp_inp)
    temp_inp = [int(x) for x in temp_inp]
    inp_items.append(temp_inp)

# all_answer = []
max_val = -1
for i in range(0, N, 1):
    for j in range(0, M, 1):
        for n_add in range(-N, N, 1):
            for m_add in range(-M, M, 1):
                if (n_add == 0 and m_add == 0):
                    continue
                a = i
                b = j
                now_num = 0
                while True:
                    if (
                        a >= N or b >= M
                        or a < 0 or b < 0
                    ):
                        break
                    
                    now_num *= 10
                    now_num += inp_items[a][b]
                    
                    if is_full_num(now_num):
                        # all_answer.append(now_num)
                        max_val = now_num if max_val < now_num else max_val
                    a += n_add
                    b += m_add

print(max_val)