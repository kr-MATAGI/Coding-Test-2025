'''
https://school.programmers.co.kr/learn/courses/30/lessons/42579

장르별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려고 함

노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같음

1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.


'''

def solution(genres, plays):
    answer = []

    '''
        {
            "classic": {
                count: 0,
                ids: [(id, plays), ... ]
            }
        }
    '''
    best_infos = {}

    input_size = len(genres)
    for idx in range(input_size):
        gen = genres[idx]
        play = plays[idx]

        if not gen in best_infos.keys():
            best_infos[gen] = {
                "count": 1,
                "sum_plays": play,
                "ids": [ (idx, play) ]
            }
        else:
            best_infos[gen]["count"] += 1
            best_infos[gen]["sum_plays"] += play
            best_infos[gen]["ids"].append((idx, play))

    # Calc
    best_infos = list(best_infos.values())
    best_infos = sorted(best_infos, key=lambda x: x["sum_plays"], reverse=True)

    for item in best_infos:
        ids = item['ids']
        ids.sort(key=lambda x: (x[1], -x[0]), reverse=True)
        ids = ids[:2]
        for id, _ in ids:
            answer.append(id)

    return answer



### MAIN ###
if "__main__" == __name__:
    ans_1 = solution(
        ["classic", "pop", "classic", "classic", "pop"],
        [500, 600, 500, 800, 2500]
    )
    print(f"ans_1: {ans_1}")
