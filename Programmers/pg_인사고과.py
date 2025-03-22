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
    
    '''
        1. 인센티브 못 받는 경우 (두 점수 미만 경우) 찾기
    '''
    lose_infos = [[], []] # 점수1, 점수2 Idx
    
    # 1, 2 점수를 나눠서 계산 
    score_1_infos = [] # [인덱스, 점수]
    score_2_infos = []
    
    for idx, (sc_1, sc_2) in enumerate(scores):
        score_1_infos.append((idx, sc_1))
        score_2_infos.append((idx, sc_2))
    score_1_infos.sort(key=lambda x: x[1])
    score_2_infos.sort(key=lambda x: x[1])
    
    wan_1_sc = scores[0][0]
    wan_2_sc = scores[0][1]
    # lose_info 에 넣기 (완호 기준으로만 검색)
    sc_1_end = False
    sc_2_end = False
    for step in range(len(score_1_infos)):
        if sc_1_end and sc_2_end:
            break
        
        # 점수 1 검사
        if not sc_1_end:
            if (
                0 != score_1_infos[step][0] or 
                wan_1_sc < score_1_infos[step][1]
            ):
                lose_infos[0].append(score_1_infos[step][0])
            
            elif 0 == score_1_infos[step][0]:
                sc_1_end = True
        
        # 점수 2 검사
        if not sc_2_end:
            if (
                0 != score_2_infos[step][0] or
                wan_2_sc < score_2_infos[step][1]
            ):
                lose_infos[0].append(score_2_infos[step][0])
            
            elif 0 == score_2_infos[step][0]:
                sc_2_end = True
    ###    
    lose_infos[0].extend(lose_infos[1])
    double_loose = list(set(lose_infos[0]))
    wan_no_incen = True if (len(lose_infos[0]) + len(lose_infos[1])) != len(double_loose) else False
    
    '''
        2. 점수 합으로 석차 구하기
    '''
    sum_scores = [] # [인덱스, 점수 합]
    for idx, sc in enumerate(scores):
        sum_scores.append((idx, sum(sc)))
    
    sum_scores.sort(key=lambda x: x[1], reverse=True)
    
    # 석차 계산
    idx_0_rank = 0
    rank_num = 0
    prev_score = -1
    same_rank_stack = 0
    rank_infos = [] # [인덱스, 점수 합, 랭크]
    for sc in sum_scores:
        if prev_score == sc[1]:
            # 동일 석차
            rank_infos.append((sc[0], sc[1], rank_num))
            same_rank_stack += 1
        else:
            rank_num += (1 + same_rank_stack)
            same_rank_stack = 0 # 누적치 초기화
            prev_score = sc[1]
            
            rank_infos.append((sc[0], sc[1], rank_num))
    
    rank_infos.sort(key=lambda x: x[0])
    answer = rank_infos[0][-1] if not wan_no_incen else -1
    return answer