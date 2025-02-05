"""
    숫자 카드는 정수 하나가 있는 카드이다.
    상근이는 숫자 카드 N개를 가지고 있다.
    정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램
"""

# 입력 처리
N = int(input()) # N은 500,000
n_list = list(map(int, input().split()))
# N 정수는 -10,000,000 <= N <= 10,000,000

M = int(input()) # M은 500,000
m_list = list(map(int, input().split())) 
# M 정수는 -10,000,000 <= N <= 10,000,000


# 계산
answers = []

'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

10
6 3 2 10 10 10 -10 -10 7 3
1
10

10
6 3 2 10 10 10 -10 -10 7 3
1
-10

10
3 3 2 10 10 10 -10 -10 3 3
1
3
'''
n_list.sort()
n_counts = {}
for n_item in n_list:
    if n_item in n_counts.keys():
        n_counts[n_item] += 1
    else:
        n_counts[n_item] = 1

for m_item in m_list:
    if m_item in n_counts.keys():
        answers.append(n_counts[m_item])
    else:
        answers.append(0)

# 출력
print(" ".join([str(x) for x in answers]))