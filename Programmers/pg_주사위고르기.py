'''
    A와 B가 n개의 주사위를 가지고 승부

    각 주사위는 1~n의 번호를 가지고 있음, 주사위에 쓰인 수의 구성도 모두 다름

    A가 먼저 n/2 개의 주사위를 가지고 가면 B가 남은 n/2개의 주사위를 가지고 간다.
    주사위를 모두 굴린뒤 합산으로 승부

    A는 자신이 승리할 확률이 가장 높아지도록 주사위를 가질려고 함
'''
from itertools import combinations, product
from collections import Counter

def solution(dice):
    answer = []

    dice_cnt = len(dice)
    dice_ids = list(range(dice_cnt))
    half_val = dice_cnt // 2
    max_win = -1

    # A, B의 가능한 모든 점수 조합을 계산
    def get_all_sums(dices):
        all_rolls = list(product(*[dice[i] for i in dices]))
        sums = [sum(tup) for tup in all_rolls]
        return Counter(sums)

    # A 가 고를 수 있는 모든 조합
    for a_dice in combinations(dice_ids, half_val):
        b_dice = [i for i in dice_ids if i not in a_dice]

        a_sums = get_all_sums(a_dice)
        b_sums = get_all_sums(b_dice)

        # B의 누적합 준비 (누적 패 개수)
        b_keys_sorted = sorted(b_sums)
        b_cum = []
        b_total = 0
        for k in b_keys_sorted:
            b_total += b_sums[k]
            b_cum.append((k, b_total))

        # A가 이기는 경우의 수 계산
        win_count = 0
        for a_score, a_count in a_sums.items():
            for b_score, b_count_cum in b_cum:
                if b_score >= a_score:
                    break
                win_count += a_count * b_sums[b_score]

        if win_count > max_win:
            max_win = win_count
            best_combo = list(a_dice)

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