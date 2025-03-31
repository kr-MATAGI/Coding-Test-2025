'''
https://school.programmers.co.kr/learn/courses/30/lessons/67258

쇼핑을 할 때 매장 진열대의 특정 범위의 물건들을 모두 싹쓸이 구매하는 습관이 있음
아래의 목적을 달성하고자 함
진열된 모들 종류의 보석을 모두 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

'''

def solution(gems):
    '''
        1) 고유한 값들 보관
        2) s와 e를 통해 자릿수 인덱싱
        3) e를 앞세워서 고유한 값들 최소 1개씩 포함될때까지 앞으로 이동
        4) 다 찾으면 s를 하나씩 줄임
    '''
    answer = []

    # 고유한 값들 확인
    target_set = set(gems)

    # 현재 보석 보유량 확인할 dict
    gem_cnt_info = {x: 0 for x in target_set}
    # print(cur_gem_info)

    # 계산
    s, e = 0, 0 # start_idx, end_idx

    cur_set = set() # 현재 중복제거한 보석들
    while True:
        cur_gem = gems[e]
        gem_cnt_info[cur_gem] += 1
        cur_set.add(cur_gem)
        if cur_set == target_set:
            # 모든 보석이 1개 이상씩 존재
            break

        e += 1

    # s를 1씩 높여가봄
    while True:
        cur_gem = gems[s]
        # print(f"s: {s}, cur_gem: {cur_gem}, gem_cnt_info: {gem_cnt_info[cur_gem]}")
        if 1 <= gem_cnt_info[cur_gem] - 1:
            # 해당 보석이 아직 1개 이상 있음
            gem_cnt_info[cur_gem] -= 1
            s += 1
        else:
            break

    answer = [s + 1, e + 1]
    return answer


if "__main__" == __name__:
    ans_1 = solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
    print(f"ans_1: {ans_1}\n")

    ans_2 = solution(["AA", "AB", "AC", "AA", "AC"]	)
    print(f"ans_2: {ans_2}\n")

    ans_3 = solution(["XYZ", "XYZ", "XYZ"])
    print(f"ans_3: {ans_3}\n")

    ans_4 = solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	)
    print(f"ans_4: {ans_4}\n")

    ans_5 = solution(["A", "B", "C", "A", "A", "B", "C", "C"])
    print(f"ans_5: {ans_5}\n")