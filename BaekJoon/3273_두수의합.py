'''
    n 개의 서로 다른 양의 정수로 이루어진 수열이 있다.
    
    a_i의 값은 1 <= a_i <= 1,000,000

    자연수 x가 주어졌을 때,
        a_i + a_j = x를 만족하는 (a_i, a_j) 쌍의 수를 구하는 프로그램을 작성하시오.
        ( i <= i < j <= n )

    * 풀이방법
        - 배열에 현 재존재하는 숫자들을 마킹
        - 순서대로 숫자 뺌
'''

# Global
X_MAX= 2000000 # 2,000,000
N_MAX = 1000000 # 1,000,000

# 입력
N = int(input())
num_arr = list(map(int, input().split()))
num_arr.sort()
X = int(input())

# 계산
existed_num_list = [ False for _ in range(N_MAX + 1)]
for num in num_arr:
    existed_num_list[num] = True

answer = 0
for num in num_arr:
    diff_val = X - num
    if diff_val <= N_MAX and existed_num_list[diff_val]:
        answer += 1

print(answer // 2)