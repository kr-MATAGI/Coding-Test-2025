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
    info_size = len(info)
    
    INF = float('inf')
    DP = [INF] * n # dp[i]는 A 흔적 합이 x일 때, b 흔적 합의 최소값
    DP[0] = 0

    # Calc
    for i in range(info_size):
        a_cost = info[i][0]
        b_cost = info[i][1]

        new_dp = [INF] * n
        for a_trace in range(n):
            if DP[a_trace] == INF:
                continue # 현재 상태가 유효하지 않음
                
            b_trace = DP[a_trace]
            
            # 물건 i를 A 가 훔침
            new_a = a_trace + a_cost
            if new_a < n:
                new_dp[new_a] = min(new_dp[new_a], b_trace)

            # 물건 i를 b가 훔침
            new_b = b_trace + b_cost
            if new_b < m:
                new_dp[a_trace] = min(new_dp[a_trace], new_b)
        DP = new_dp
    
    # 모든 물건 처리가 끝난 뒤,
    # dp[x] != INF 이고 dp[x] < m 인 x 중 최솟값을 찾는다.
    answer = min([x for x in range(n) if DP[x] < m], default=INF)
    return answer if answer != INF else -1

### MAIN ###
if "__main__" == __name__:
    # ans_1 = solution(
    #     [[1, 2], [2, 3], [2, 1]],
    #     4, 4
    # )
    # print(ans_1)

    ans_2 = solution(
        [[3, 3], [3, 3]],
        7, 1
    )
    print(ans_2)