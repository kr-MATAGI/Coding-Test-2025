'''
https://school.programmers.co.kr/learn/courses/30/lessons/340212?language=python3'


순서대로 N개의 퍼즐을 제한 시간내에 풀어야 하는 퍼즐 게임을 하고 있다.
각 퍼즐은 난이도와 소요 시간이 정해져 있다.

나의 숙련도에 따라 퍼즐을 풀 때, 틀리는 횟수가 바뀐다.

현재 퍼즐의 난이도 : diff
나의 숙련도 : level

1) diff <= level : 퍼즐 틀리지 않고, time_cur 만큼의 시간을 사용하여 해결

2) diff > level : diff - level 번 틀린다
                  틀릴때마다 time_cur 만큼의 시간을 사용
                  추가로 time_prev 만큼의 시간을 사용해 이전 퍼즐을 다시 풀고 와야한다.
                  이전 퍼즐을 다시 풀 때는 난이도에 상관없이 틀리지 않는다.
                  diff - level 번 틀린 이후에 다시 퍼즐을 풀면 time_cur 만큼의 시간을 사용하여 퍼즐을 해결

퍼즐 게임에는 전체 제한 시간 limit가 정해져 있다.
제한 시간 내에 퍼즐을 모두 해결하기 위한 숙련도의 최솟값을 구하라


숙련도의 시작점은 어떻게 잡을 것인가?

어떤 방법으로 해결할 것인가?
    1) 단순 순회는 안됨 
    2) DFS, BFS 안됨

예1:
    1, 5, 3     [2,4,7]     30
    (1 ~ 5)
    1) 5
        2
        4
        7
        = 13
    
    2) 4
        2
        (4 + 2) * 1 + 4 = 10
        7
        = 19
    
    3) 3
        2
        (4 + 2) * 2 + 4 = 16
        7
        = 25

예2:
    [1, 328, 467, 209, 54]
    [2, 7, 1, 4, 3]
    1723

    1) 294
        1 -> 2
        328 -> (7+2) * 34 + 7 = 313
        467 -> (1+7) * 173 + 1 = 1385
        209 -> 4
        54 -> 3

'''
def solution(diffs, times, limit):
    '''
        제한 시간 내에 퍼즐을 모두 해결하기 위한 숙련되의 최솟값
    '''
    ret_val = 0

    # Calc
    max_val = max(diffs)
    min_val = min(diffs)
    
    all_levels = []
    while True:
        mid_val = (max_val + min_val) // 2
        
        if mid_val == max_val or min_val == mid_val:
            break
        
        total_time = 0
        for step, (cur_diff, cur_time) in enumerate(zip(diffs, times)):
            if cur_diff <= mid_val: # 틀리지 않음
                total_time += cur_time
            else:
                wrong_cont = cur_diff - mid_val
                prev_time = 0
                if 0 < step:
                    prev_time = times[step - 1]
                spend_time = ((cur_time + prev_time) * wrong_cont) + cur_time
                total_time += spend_time
        
        if total_time > limit:
            # min 변경
            min_val = mid_val
        else:
            all_levels.append(mid_val)
            max_val = mid_val
                
    ret_val = min(all_levels)
    return ret_val


if "__main__" == __name__:
    ans_1 = solution(
        [1,5,3],
        [2,4,7],
        30
    )

    ans_2 = solution(
        [1,4,4,2],
        [6,3,8,2],
        59
    )

    ans_3 = solution(
        [1,328,467,209,54],
        [2,7,1,4,3],
        1723
    )

    ans_4 = solution(
        [1, 99999, 100000, 99995],
        [9999, 9001, 9999, 9001],
        3456789012
    )

    print(f"ans_1: {ans_1}")
    print(f"ans_2: {ans_2}")
    print(f"ans_3: {ans_3}")
    print(f"ans_4: {ans_4}")