import sys
input = sys.stdin.readline

"""
    자판기의 특정 버튼을 순서대로 누르면, 평소와 다른 색깔의 식권이 나온다.

    버튼 조작 중 비밀 메뉴 조작법이 포함되어 있는지를 판단하는 회로 추가

    자판기에는 총 K개의 버튼이 있다. (1~K)
    버튼 조합은 1이상 K개 이하의 정수 여러개

    비밀 메뉴 조작법은 M개의 버튼 조작으로 이루어짐, 순서대로 눌러야함
    이 조작법 앞뒤로 다른 버튼 조작이 있어도 비밀 메뉴로 인정됨.

    사용자가 누른 N개의 조작이 주어질때, 비밀메뉴를 받을 수 있는지 확인
"""

# 입력
# 비밀메뉴 버튼 개수
# 사용자가 누른 조작 수
# 자판기 버튼 개수
M, N, K = map(int, input().strip().split())
m_list = list(map(int, input().strip().split()))
n_list = list(map(int, input().strip().split()))

# 계산
is_secret = False
for i in range(N):
    if i+M > N:
        break

    cur_val = n_list[i:i+M]
    # print(cur_val)

    if cur_val == m_list:
        is_secret = True
        


# 출력
if is_secret:
    print('secret')
else:
    print('normal')