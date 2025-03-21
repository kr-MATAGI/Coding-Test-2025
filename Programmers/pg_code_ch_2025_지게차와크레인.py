'''
    알파벳 대문자로 종류를 구붛나는 컨테이너 세로 n, 가로 m
    
    특정 종류 컨테이너의 출고 요청이 들어올 때마다 지게차로 창고에서 접근이 가능한 해당 종류의 컨테이너를 모두 꺼낸다.
        * 접근이 가능한 컴테이너 = 4면 중 적어도 1면이 창고 외부와 연결된 컨테이너
    
    크레인을 사용하면 요청된 종류의 모든 컨테이너를 꺼낸다
        * 알파벳 1개만 -> 지게차로
        * 알파벳 2개 -> 크레인으로
        
    모든 요청을 완료하고, 남은 컨테이너의 수를 출력
    
    
'''
from collections import deque

def solution(storage, requests):
    answer = 0
    
    # Init
    row_len = len(storage) + 2
    col_len = len(storage[0]) + 2
    new_store = [ ['-' for _ in range(col_len) ] for _ in range(row_len) ] 
    # visited = [ [False for _ in range(col_len) ] for _ in range(row_len) ]
    
    '''
        ['-', '-', '-', '-', '-', '-', '-']
        ['-', 'A', 'Z', 'W', 'Q', 'Y', '-']
        ['-', 'C', 'A', 'A', 'B', 'X', '-']
        ['-', 'B', 'B', 'D', 'D', 'A', '-']
        ['-', 'A', 'C', 'A', 'C', 'A', '-']
        ['-', '-', '-', '-', '-', '-', '-']
        
        ['-', '-', '-', '-', '-', '-', '-']
        ['-', '-', 'Z', 'W', 'Q', 'Y', '-']
        ['-', 'C', 'A', 'A', '-', 'X', '-']
        ['-', '-', '-', 'D', 'D', '-', '-']
        ['-', '-', 'C', '-', 'C', '-', '-']
        ['-', '-', '-', '-', '-', '-', '-']
        
        -> 여기서 A를 꺼낼 때 상화좌우만 봐서는 안된다.
        
        ['-', '-', '-', '-', '-']
        ['-', 'H', 'A', 'H', '-']
        ['-', 'H', 'B', 'H', '-']
        ['-', 'H', 'H', 'H', '-']
        ['-', 'H', 'A', 'H', '-']
        ['-', 'H', 'B', 'H', '-']
        ['-', '-', '-', '-', '-']

        [False, False, False, False, False]
        [False, False, False, False, False]
        [False, False, False, False, False]
        [False, False, False, False, False]
        [False, False, False, False, False]


        ['-', '-', '-', '-', '-']
        ['-', 'H', 'H', 'H', '-']
        ['-', 'H', 'H', 'H', '-']
        ['-', 'H', 'A', 'H', '-']
        ['-', 'H', 'H', 'H', '-']
        ['-', 'H', 'H', 'H', '-']
        ['-', '-', '-', '-', '-']
    '''
    
    pos_infos = {}
    for rdx in range(row_len - 2):
        for cdx in range(col_len - 2):
            new_store[rdx+1][cdx+1] = storage[rdx][cdx]
            answer += 1
            
            if not new_store[rdx+1][cdx+1] in pos_infos.keys():
                pos_infos[new_store[rdx+1][cdx+1]] = [(rdx+1, cdx+1)]
            else:
                pos_infos[new_store[rdx+1][cdx+1]].append((rdx+1, cdx+1))
    

    # Calc
    def is_able_move_container(
        store, 
        cr, cc,
        visited,
    ):
        '''
            DFS -> BFS
            상화좌우로 끝까지 가봐서 뚤려있으면 ok
        '''
        visited[cr][cc] = True

        que = deque()
        que.append([cr, cc])
    
        # 상하좌우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while que:
            cur_item = que.popleft()

            # 끝에 도달
            if (
                (0 == cur_item[0] or cur_item[0] == row_len - 1) or
                (0 == cur_item[1] or cur_item[1] == col_len - 1)
            ): 
                if '-' == store[cur_item[0]][cur_item[1]]: # 뚤려있음
                    return True

            for d in range(4):
                next_r = cur_item[0] + dx[d]
                next_c = cur_item[1] + dy[d]

                if not (0 <= next_r < row_len and 0 <= next_c < col_len):
                    continue
                elif visited[next_r][next_c]:
                    continue
                elif "-" != store[next_r][next_c]: 
                    # 막혀있으니까 볼 필요 없음
                    continue
                
                visited[next_r][next_c] = True
                que.append([next_r, next_c])
        
        return False
    ###
    
    for req_item in requests:
        remove_items = []
        
        target_ch = ""
        if 1 == len(req_item):
            if not req_item in pos_infos.keys():
                continue
            
            target_ch = req_item
            # 지게차 사용
            for r, c in pos_infos[req_item]:
                if req_item == new_store[r][c]:
                    visited = [ [False for _ in range(col_len) ] for _ in range(row_len) ]
                    # print(f"{req_item}, {[r, c]}, {pos_infos[req_item]}")                    
                    is_moving = is_able_move_container(
                        new_store,
                        r, c,
                        visited
                    )
                    # print(f"[{r},{c}] - {new_store[r][c]}, {is_moving}\n")
                        
                    if is_moving:
                        remove_items.append((r,c)) # 컨테이너를 뺌
                    
        else:
            if not req_item[0] in pos_infos.keys():
                continue

            target_ch = req_item[0]
            # 크레인 사용
            for r, c in pos_infos[req_item[0]]:
                remove_items.append((r,c)) # 컨테이너를 뺌

        # 뺀 컨테이너 정리
        for r, c in remove_items:
            new_store[r][c] = '-'
            answer -= 1

            pos_infos[target_ch].remove((r,c))
            # print(f"target: {target_ch}\n{pos_infos[target_ch]}")
            
    
    for a in new_store:
        print(a)
    
    return answer


### MAIN ###
if "__main__" == __name__:
    ans_1 = solution(
        ["AZWQY", "CAABX", "BBDDA", "ACACA"],
        ["A", "BB", "A", 'C', 'Q', 'AA'],
    )
    print(ans_1)

    ans_2 = solution(
        ["HAH", "HBH", "HHH", "HAH", "HBH"],
        ["C", "B", "B", "B", "B", "H", 'A', "H", "BB"]
    )
    print(ans_2)

    ans_3 = solution(
        ['HHH', 'HHH' 'HHH', 'HAH', 'HAH', 'HHH', 'HHH'],
        ['AA', 'H']
    )

    '''
        ['-', '-', '-', '-', '-', '-']
        ['-', 'A', 'A', 'A', 'A', '-']
        ['-', 'A', '-', 'A', 'A', '-']
        ['-', 'A', '-', 'A', 'A', '-']
        ['-', 'A', '-', 'A', 'A', '-']
        ['-', '-', '-', '-', '-', '-']
    '''
    ans_4 = solution(
        ["AAAA", "ABAA", "ABAA", "ACAA"],
        # ['CC','BB','A']
        # ["CC"]
        # ["CC", "BB"]
        ["CC", "BB", 'A']
    )