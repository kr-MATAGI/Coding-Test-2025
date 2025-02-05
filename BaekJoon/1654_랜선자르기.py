"""
    N개의 랜선을 만들어야 함
    이미 자체적으로 길이가 제각각인 K 개의 랜선을 가지고 있다.

    하지만 길이가 같은 N개의 랜선으로 만들고 싶다.
    랜선을 자르거나 만들 때, 손실되는 길이는 없다 (이미 자른 랜선은 붙일 수 없다.)
    

    이때 만들 수 있는 최대 랜선의 길이

"""

'''
4 11
802
743
457
539

4 1
800
700
400
500

802 -> 4개
743 -> 3개
457 -> 2개
539 -> 2개
-->>>>11개
'''

# 입력
K, N = map(int, input().split())
lan_lines = []
for _ in range(K):
    lan = int(input())
    lan_lines.append(lan)


# 계산
total_lan_lens = sum(lan_lines) # 2541
optim_lan_len = sum(lan_lines) // N # 231

low = 1
high = optim_lan_len

ans = 0
while low <= high:
    mid = (low + high) // 2
    
    lan_cable_slice_val = sum([x // mid for x in lan_lines])
    
    if N <= lan_cable_slice_val:
        ans = mid
        low = mid + 1
        
    # elif N < lan_cable_slice_val:
    #     low = mid + 1
    
    else:
        high = mid - 1

# print('----\n')
# print(optim_lan_len)

# 출력
print(ans)