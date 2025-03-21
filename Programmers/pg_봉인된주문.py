'''
    각 주문은 알파벳 소문자 11글자 이하로 구성되어 있음

    모든 문자열이 아래 규칙에 따라 정렬되어 있음
        1) 글자 수가 적은 주문부터 기록된다.
        2) 글자 수가 같다면, 알파벳 순서대로 기록된다.

    몇몇 주문을 주문서에서 삭제되었음
    삭제가 완료된 주문서에서 n번째 주문을 찾아내야 한다.

'''
from itertools import product

def solution(n, bans):
    valid_spells = []
    
    # 길이 1~11까지 가능한 모든 문자열을 사전 순서대로 생성
    for length in range(1, 12):  # 1~11 길이의 문자열 생성
        for spell in map("".join, product("abcdefghijklmnopqrstuvwxyz", repeat=length)):
            valid_spells.append(spell)

    # 삭제할 주문 제거
    valid_spells = [spell for spell in valid_spells if spell not in set(bans)]

    # n번째 주문 찾기
    return valid_spells[n-1]

### MAIN ###
if "__main__" == __name__:
    ans_1 = solution(
        30, ["d", "e", "bb", "aa", "ae"]	
    )
    print(f"ans_1: {ans_1}\n")


    ans_2 = solution(
        7388, ["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"]
    )
    print(f"ans_2: {ans_2}\n")