'''
    연말마다 1년 간의 인사고과에 따라 인센티브 지급
    
    각 사원마다 근무 태도 점수와 동료 평가 점수가 기록되어 있는데
    
    만약 어떤 사원이 다른 임의의 사원보다 두 점수가 모두 낮은 경우가 한 번이라도 있다면
    그 사원은 인센티브를 받지 못 한다.
    
    그렇지 않은 사원들에 대해서는 두 점수의 합이 높은 순으로 석차를 내어 석차에 따라 인센티브가 지급된다.
    동석차의 수 만큼 다음 석차는 건너 뛴다.
    
    완호[0]가 인센티브를 받지 못하는 경우 -1을 출력
    
'''
def solution(scores):
    
    answer = 0 
    
    scores_sorted = sorted(scores, key=lambda x: (-x[0], x[1])) # 태도 내림차순, 동료 오름차순
    
    wanho_score = scores[0]
    max_peer = 0
    filtered = []
    
    for att, peer in scores_sorted:
        if peer < max_peer:
            continue
        
        max_peer = max(peer, max_peer)
        filtered.append([att, peer])
    
    print(scores_sorted)
    # print(filtered)
    
    # 원호는 인센 못 받음
    if not wanho_score in filtered:
        return -1
    
    # 랭크
    sum_scores = [sum(x) for x in filtered]
    sum_scores.sort(reverse=True)
    
    rank = 0
    prev_sc = -1
    stack = 0
    
    for sc in sum_scores:
        if sc == prev_sc:
            stack += 1
        else:
            rank += (1 + stack)
            stack = 0
            prev_sc = sc
            
        if sc == sum(wanho_score):
            return rank
    
    return answer

### MAIN ###
if "__main__" == __name__:
    ans_1 = solution(
        [[2,2],[3,4],[3,2],[3,2],[2,1]]	
    )
    print(ans_1)