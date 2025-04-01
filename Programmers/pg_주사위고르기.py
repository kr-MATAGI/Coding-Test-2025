'''
    A와 B가 n개의 주사위를 가지고 승부

    각 주사위는 1~n의 번호를 가지고 있음, 주사위에 쓰인 수의 구성도 모두 다름

    A가 먼저 n/2 개의 주사위를 가지고 가면 B가 남은 n/2개의 주사위를 가지고 간다.
    주사위를 모두 굴린뒤 합산으로 승부

    A는 자신이 승리할 확률이 가장 높아지도록 주사위를 가질려고 함
'''
from collections import defaultdict


def solution(dice):
    answer = []

    dice_win_info = defaultdict(int)

    dice_len = len(dice)
    for b_idx, base_dice in enumerate(dice):
        dice_win_info[b_idx] = defaultdict(int)

        for o_idx, other_dice in enumerate(dice):
            if o_idx == b_idx:
                continue

            # 숫자가 다른 다이스에서 몇 번 이길 수 있는지 계산
            for b_num in base_dice:
                for o_num in other_dice:
                    if b_num > o_num:
                        dice_win_info[b_idx][b_num] += 1

    # print(dice_win_info)
    dice_total_wins = {i + 1: 0 for i in range(dice_len)}
    # 다이스-눈금 별 이긴 횟수 총합
    for dice_id, dice_num_wins in dice_win_info.items():
        for win in dice_num_wins.values():
            dice_total_wins[dice_id + 1] += win
    # 정렬
    sorted_wins = list(dice_total_wins.items())
    sorted_wins.sort(key=lambda x: x[1], reverse=True)
    print(sorted_wins)
    sorted_wins = sorted_wins[:dice_len // 2]

    answer = [x[0] for x in sorted_wins]
    answer.sort()
    return answer