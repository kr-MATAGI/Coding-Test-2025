import sys
input = sys.stdin.readline

'''
    학번 구간이 주어질때 이 학생들의 성적 평균을 구하는 프로그램
'''

# 입력
N, K = map(int, input().strip().split()) # 학생 수, 구간 수

# 학생의 성적
student_scores = [0]
student_scores.extend(list(map(int, input().strip().split())))

# 구간 A, B
k_list = []
for _ in range(K):
    temp = list(map(int, input().strip().split()))
    k_list.append(temp)

# 10 + 50 + 20 = 80 / 3 = 26.6666666
# 계산 - Maybe 누적합
'''
    10 50 20  70  100
    10 60 80 150  250

    1 - 3 : 80 / 3
    3 - 4 : 150 - 60 = 90
    1 - 5 : 250 / 5 = 50
'''
calc_arr = [ 0 for _ in range(N+1) ]

# 누적합 만들기
calc_arr[1] = student_scores[1]
for i in range(2, N+1):
    calc_arr[i] = student_scores[i] + calc_arr[i-1]

# 질문에 따른 결과 출력
answer_list = []
for k_item in k_list:
    left_idx = k_item[0]
    right_idx = k_item[1]

    ans = 0
    if left_idx == 1:
        ans = round(calc_arr[right_idx] / (right_idx - left_idx + 1), 2)
    else:
        ans = round((calc_arr[right_idx] - calc_arr[left_idx-1]) / (right_idx - left_idx + 1), 2)
    
    answer_list.append(ans)

for ans in answer_list:
    print("%(ans)0.2f" % {"ans": ans})