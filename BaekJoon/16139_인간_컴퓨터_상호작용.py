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


* 부분점수
    - 그저 list slice 사용하면 효율이 없음
"""

MAX_S = 200000 # 200,000
MAX_Q = 200000 # 200,000


# 입력
S = list(str(input()))
Q = int(input())

q_list = []
for _ in range(Q):
    a, l, r = map(str, input().split())
    l = int(l)
    r = int(r)
    q_list.append((a, l, r))

# 계산
calc_arr = [ [] for _ in range(26) ] # 알파벳: [] -> 정보 저장

minus_alpha_val = ord('a')
for sdx, s_char in enumerate(S):
    char2int = ord(s_char.lower()) - minus_alpha_val

    calc_arr[char2int].append(sdx)

# 출력
for a, b, c in q_list:
    its_me = calc_arr[ord(a) - minus_alpha_val]

    answer = 0
    for i in its_me:
        if b <= i <= c:
            answer += 1
    
    print(answer)