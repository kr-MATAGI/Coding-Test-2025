'''
    A와 B가 n개의 주사위를 가지고 승부

    각 주사위는 1~n의 번호를 가지고 있음, 주사위에 쓰인 수의 구성도 모두 다름

    A가 먼저 n/2 개의 주사위를 가지고 가면 B가 남은 n/2개의 주사위를 가지고 간다.
    주사위를 모두 굴린뒤 합산으로 승부

    A는 자신이 승리할 확률이 가장 높아지도록 주사위를 가질려고 함
'''
from itertools import combinations, product
from typing import List
from collections import Counter

def solution(dice: List[List[int]]) -> List[int]:
    n = len(dice)                 # 주사위 개수
    half = n // 2                 # A, B가 각각 가질 주사위 개수
    dice_idx = list(range(n))    # 주사위 인덱스 (0부터 n-1까지)
    max_win = -1                 # A의 최대 승리 횟수 저장용
    best_combo = []              # A가 선택할 최적 주사위 조합

    # A가 고를 수 있는 모든 주사위 조합을 순회
    for a_dice in combinations(dice_idx, half):
        b_dice = [i for i in dice_idx if i not in a_dice]  # B는 나머지 주사위 선택

        # 해당 조합에서 주사위로 나올 수 있는 모든 점수 합을 구하는 함수
        def get_all_sums(dice_group):
            all_rolls = list(product(*[dice[i] for i in dice_group]))  # 각 주사위의 눈을 곱집합으로 생성
            sums = [sum(tup) for tup in all_rolls]                     # 각 경우의 점수 합
            return Counter(sums)  # 각 합이 몇 번 나오는지 세어줌 (딕셔너리 형태)

        a_sums = get_all_sums(a_dice)  # A가 낼 수 있는 모든 점수 합 분포
        b_sums = get_all_sums(b_dice)  # B가 낼 수 있는 모든 점수 합 분포

        # B의 점수들을 오름차순 정렬하고 누적합 계산
        # → A가 특정 점수를 냈을 때, 그보다 낮은 B의 점수가 몇 개나 되는지 빠르게 알기 위함
        b_keys_sorted = sorted(b_sums)
        b_cum = []
        b_total = 0
        for k in b_keys_sorted:
            b_total += b_sums[k]
            b_cum.append((k, b_total))

        # A가 이기는 경우의 수 계산
        win_count = 0
        for a_score, a_count in a_sums.items():
            # A 점수보다 낮은 B 점수에 대해서만 승리 가능
            for b_score, _ in b_cum:
                if b_score >= a_score:
                    break
                win_count += a_count * b_sums[b_score]
                # A가 해당 점수를 낼 경우, B가 b_score을 낼 확률만큼 승리 횟수 누적

        # 지금까지 중 가장 높은 승리 수라면 저장
        if win_count > max_win:
            max_win = win_count
            best_combo = list(a_dice)

    # 결과는 1-indexed로 정답 출력
    return [i + 1 for i in sorted(best_combo)]


### MAIN ###
if "__main__" == __name__:
    ans_1 = solution(
        [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
    )
    print(f"ans_1: {ans_1}\n")


    ans_2 = solution(
        [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]
    )
    print(f"ans_2: {ans_2}\n")

    ans_3 = solution(
        [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
    )
    print(f"ans_3: {ans_3}\n")