'''
https://school.programmers.co.kr/learn/courses/30/lessons/67258

쇼핑을 할 때 매장 진열대의 특정 범위의 물건들을 모두 싹쓸이 구매하는 습관이 있음
아래의 목적을 달성하고자 함
진열된 모들 종류의 보석을 모두 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

'''
from collections import defaultdict

def solution(gems):
    '''
        1) 고유한 값들 보관
        2) left와 right를 이용해서 계산
        3) right를 하나씩 옮김 -> 다 찾았는가 -> left 옮김
        4) left 옮겼을 때 최소 거리 갱신 -> 0으로 되면 해당 삭제 -> 다시 rigth 옮길 수 있도록
    '''
    answer = []
    min_dist = len(gems)

    # 고유한 값들 확인
    target_set = set(gems)

    # 현재 보석 보유량 확인할 dict
    gem_cnt_info = defaultdict(int)
    gem_cnt_info[gems[0]] = 1

    # 계산
    left, right = 0, 0
    while left <= right < len(gems):
        if len(gem_cnt_info) != len(target_set):
            # 아직 모든 종류를 포함하지 않음
            right += 1
            if right >= len(gems):
                break
            gem_cnt_info[gems[right]] += 1
        else:
            # 모든 종류가 포함되었으면 왼쪽 줄이기
            if right - left < min_dist:
                answer = [left + 1, right + 1]
                min_dist = right - left
            gem_cnt_info[gems[left]] -= 1
            if gem_cnt_info[gems[left]] == 0:
                del gem_cnt_info[gems[left]]
            left += 1

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

    ans_6 = solution(["A", "A", "B", "B", "B", "C", "C", "A", "A", "B", "C"])
    print(f"ans_6: {ans_6}\n")