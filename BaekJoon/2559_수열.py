'''
    연속된 합의 가장 큰 것

10 2
3 -2 -4 -9 0 3 7 13 8 -3

-> 21

10 5
3 -2 -4 -9 0 3 7 13 8 -3

-> 31

10 9
3 -2 -4 -9 0 3 7 13 8 -3

-> 19

'''

# print(sum([3, -2, -4, -9, 0, 3, 7, 13, 8]))
# print(sum([-2, -4, -9, 0, 3, 7, 13, 8, -3]))

N, K = map(int, input().strip().split())
num_list = list(map(int, input().strip().split()))

# 계산
left_idx = 0
right_idx = K - 1
cur_val = sum(num_list[left_idx:right_idx + 1])
max_val = cur_val

right_idx += 1
for i in range(K, N):
    cur_val -= num_list[left_idx]
    cur_val += num_list[right_idx]
    
    # print(left_idx, right_idx, num_list[left_idx], num_list[right_idx], cur_val)

    if cur_val > max_val:
        max_val = cur_val

    if left_idx < N - K:
        left_idx += 1
    
    if right_idx < N:
        right_idx += 1

# 출력
print(max_val)