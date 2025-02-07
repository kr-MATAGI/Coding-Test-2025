import sys
input = sys.stdin.readline

# 입력
W, N = map(int, input().rstrip().split()) # 배낭의 무게, 귀금속 종류
items = [] # [무게, 무게당 가격]
for _ in range(N):
    item = list(map(int, input().rstrip().split()))
    items.append(item)

items.sort(key=lambda x: x[1], reverse=True)

# 계산
cost = 0
for item in items:
    get_w = 0
    if 0 <= W - item[0]:
        get_w = item[0]
    else:
        get_w = W
    
    cost += (get_w * item[1])
    W -= get_w

print(cost)