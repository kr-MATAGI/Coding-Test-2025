'''
    연속 부분 합
'''
def solution(sequence):
    answer = 0
    
    plus_pulse = [1 if i % 2 == 0  else -1 for i in range(len(sequence))]
    minus_pulse = [1 if i % 2 != 0 else -1 for i in range(len(sequence))]
    
    plus_seq = [x * y for x, y in zip(sequence, plus_pulse)]
    minus_seq = [x * y for x, y in zip(sequence, minus_pulse)]

    p_max = 0
    m_max = 0
    p_val = 0
    m_val = 0
    for pi, mi in  zip(plus_seq, minus_seq):
        p_val += pi
        if p_val < 0:
            p_val = 0
        if p_val > p_max:
            p_max = p_val
        
        m_val += mi
        if m_val < 0:
            m_val = 0
        if m_val > m_max:
            m_max = m_val

    print(p_max, m_max)
    answer = max(p_max, m_max)
    return answer


### MAIN ###
if "__main__" == __name__:
    ans_1 = solution(
        [2, 3, -6, 1, 3, -1, 2, 4]
    )
    print(ans_1)