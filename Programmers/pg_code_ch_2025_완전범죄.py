'''
    각 도둑이 물건을 훔칠 때 남기는 흔적이 누적되면 경찰에 붙잡히기에 흔적을 최소화해야 한다.
    
    물건 훔치는 조건
        1) 물건 [i] 를 훔칠 때,
            - A 도둑이 훔치면 info[i][0]에 A에 대한 흔적
            - B 도둑이 훔치면 info[i][1]에 B에 대한 흔적
            
        각 물건에 대해 도둑이 남기는 흔적의 개수는 1이상 3이하
        
    경찰에 붙잡히는 조건
        - A 도둑은 자식이 남긴 흔적의 개수가 n개 이상이면 경찰에 붙잡힘
        - B 도둑은 자신이 남긴 흔적의 개수가 m개 이상이면 경찰에 붙잡힘
    
    두 도둑 모두 경찰에 붙잡히지 않도록 모든 물건을 훔쳤을 때,
    A 도둑이 남긴 흔적의 누적 개수의 최솟값을 Return
    만약, 두 도둑 모두 경찰에 붙잡힌다면 -1
'''

'''
    풀이 방식
    1) DFS
    2) DP
'''

def solution(info, n, m):
    # Init
    answer = -1

    LEN = len(info)    
    INF = float('inf')
    # dp[i][b] = i 아이템에서 B의 누적 흔적이 b일 때, A의 최소 누적 흔적
    DP = [[INF] * m for _ in range(LEN + 1)]
    DP[0][0] = 0

    # Calc
    for i in range(LEN):
        a_cost, b_cost = info[i]
        
        for b in range(m):
            if DP[i][b] == INF:
                continue

            # A가 i를 훔침
            a_steal = a_cost + DP[i][b]
            if a_steal < n:
                DP[i + 1][b] = min(DP[i + 1][b], a_steal)
            
            # B가 i를 훔침
            b_steal = b + b_cost
            if b_steal < m:
                DP[i + 1][b_steal] = min(DP[i + 1][b_steal], DP[i][b])
            
    answer = min(DP[LEN])
    return answer if answer != INF else -1

### MAIN ###
if "__main__" == __name__:
    ans_1 = solution(
        [[1, 2], [2, 3], [2, 1]],
        4, 4
    )
    print(ans_1)

    ans_2 = solution(
        [[3, 3], [3, 3]],
        7, 1
    )
    print(ans_2)