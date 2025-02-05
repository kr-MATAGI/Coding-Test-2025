"""
    "문자열에서 특정 알파벳이 몇 번 나타는지 알아봐서
    자주 나타나는 알파벳이 중지나 검지 위치에 오는 알파벳인지 확인하면 실용적인지 확인할 수 있을 것이다."
    -> 미친놈


    문자열 S
    특정 알파벳 a
    문자열의 구간 l~r

    S의 l번째 문자부터 r번째 문자 사이에 a가 몇 번 나타나는지 구하는 프로그램을 작성

    * 승재는 문자열의 문자는 0번째 부터 센다
    * l번째와 r번째를 포함한다.
    * 승재는 호기심이 많기 때문에 같은 문자열을 두고 질문을 q번 할 것임

seungjaehwang
4
a 0 5
a 0 6
a 6 10
a 7 10

seungj -> 0
seungja -> 1
aehwang -> 2
ehwang -> 1

* 풀이 방법
    1)
        - 문자열 길이 (200,000) * 알파벳 개수(26) 의 2차원 배열을 만든다.
        - 먼저 정보들을 만들어 놓는게 유리

    2)
        - 알파벳 개수 (26) * 문자열 길이 (200,000)
        -> 1번 방법에 비해 메모리랑 속도 3배 감소 확인
        -> but, 최악은 200,000 * 200,000 임


* 부분점수
    - 그저 list slice 사용하면 효율이 없음
"""

MAX_S = 200000 # 200,000
MAX_Q = 200000 # 200,000

import sys
input = sys.stdin.readline

# 입력
S = list(str(input().strip()))
Q = int(input().strip())

# 계산
calc_arr = [ [0 for _ in range(26)] for _ in range(len(S) + 1) ] # 알파벳 * 문자열 길이

minus_alpha_val = ord('a')
for sdx, s_char in enumerate(S):
    char2int = ord(s_char.lower()) - minus_alpha_val

    if 0 < sdx:
        for i in range(26):
            calc_arr[sdx][i] = calc_arr[sdx-1][i]

    calc_arr[sdx][char2int] += 1

# 출력
for _ in range(Q):
    a, l, r = map(str, input().strip().split())
    l = int(l)
    r = int(r)

    char2int = ord(a) - minus_alpha_val
    if 0 == l:
        # 최대값을 출력하면 됨
        # answers.append(str(calc_arr[r][char2int]))
        print(calc_arr[r][char2int])
    else:
        # calc_arr[char2int][c] : 0번째부터 c까지 총 등장 수
        # calc_arr[char2int][b - 1]: 0번째부터 b 직전까지의 등장 수
        # 두 개의 차는 곧 b ~ c 까지의 등장 횟수
        answer = calc_arr[r][char2int] - calc_arr[l-1][char2int]
        # answers.append(str(answer))
        print(answer)


##### 아래는 이분 탐색 사용하는 코드

import sys
import bisect

input = sys.stdin.readline
S = input().strip()
Q = int(input().strip())

# 각 알파벳(0~25)에 대해 등장하는 인덱스를 저장합니다.
positions = [[] for _ in range(26)]
for i, ch in enumerate(S):
    positions[ord(ch) - ord('a')].append(i)

# 질의 처리
for _ in range(Q):
    letter, l, r = input().split()
    l = int(l)
    r = int(r)
    idx = ord(letter) - ord('a')
    
    # positions[idx]에서 l 이상의 첫 인덱스와 r를 초과하는 첫 인덱스를 찾습니다.
    left = bisect.bisect_left(positions[idx], l)
    right = bisect.bisect_right(positions[idx], r)
    # 두 인덱스의 차이가 구간 내 등장 횟수입니다.
    sys.stdout.write(str(right - left) + "\n")