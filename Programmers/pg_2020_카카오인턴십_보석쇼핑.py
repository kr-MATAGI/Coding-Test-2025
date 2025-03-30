'''
https://school.programmers.co.kr/learn/courses/30/lessons/67258

쇼핑을 할 때 매장 진열대의 특정 범위의 물건들을 모두 싹쓸이 구매하는 습관이 있음
아래의 목적을 달성하고자 함
진열된 모들 종류의 보석을 모두 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

'''

def solution(gems):
    answer = []

    '''
        1. 보석의 중복 제거 필요 -> 2번 과정이 있으니 필요 없을 듯?
        2. 전체 길이에서 조금씩 줄여가는 것이 필요
            - 왼쪽에서 줄이다가 하나가 0이 되어버리면 줄이지 않음
            -> 오른쪽으로 줄이기 시작 -> 하나가 0이 되어버리면 줄이지 않음
    '''

    # Make Dict
    gem_infos = {}
    for gem in gems:
        if not gem in gem_infos.keys():
            gem_infos[gem] = 1
        else:
            gem_infos[gem] += 1

    # Start Calc
    left_idx = 0
    right_idx = len(gems) - 1

    is_left_end = False
    is_right_end = False

    while True:
        if is_left_end and is_right_end:
            break

        if not is_right_end:
            # 오른쪽 이동
            right_gem = gems[right_idx]
            if 1 < gem_infos[right_gem]:
                right_idx -= 1
                gem_infos[right_gem] -= 1
            else:
                is_right_end = True

        else:
            left_gem = gems[left_idx]
            if 1 < gem_infos[left_gem]:
                # 아직 해당 보석이 1개 이상이므로 진행 가능
                left_idx += 1
                gem_infos[left_gem] -= 1
            else:
                is_left_end = True

        # print(f"left - idx: {left_idx}, gem: {gems[left_idx]}, right - idx: {right_idx}, gem: {gems[right_idx]}, {gem_infos}")

    # Answer
    answer = [left_idx + 1, right_idx + 1]
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