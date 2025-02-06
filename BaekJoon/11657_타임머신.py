import sys
input = sys.stdin.readline

"""
3 4
1 2 4
1 3 3
2 3 -1
3 1 -2
"""
# 1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램

INF = float('inf')

# 입력
N, M = map(int, input().rstrip().split()) # 도시의 개수, 간선의 개수
# A: 시작도시, B: 도착도시, C: 버스를 타고 이동하는데 걸리는 시간
# C ==0 순간이동, C < 0: 타임머신으로 시간을 되돌아가는 경우
city_infos = []
for _ in range(M):
    temp = list(map(int, input().rstrip().split()))
    city_infos.append(temp)

# 계산
time_costs = [ INF for _ in range(N+1) ]
time_costs[0] = 0
time_costs[1] = 0

# 간선 완화
for i in range(M-1):
    for a, b, c in city_infos:
        if time_costs[a] != INF and time_costs[a] + c < time_costs[b]:
            time_costs[b] = time_costs[a] + c

# 음수 사이클 확인
# time_costs[a] + c < time_costs[b] -> 경로를 더 단축 시킬 수 있다.
# 음수 사이클이 존재하면, 사이클이 한 바퀴 돌떄마다 총 경로 비용이 감소하여 무한히 개선 가능

is_inf_time = False
for a,b,c in city_infos:
    if time_costs[a] != INF and time_costs[a] + c < time_costs[b]:
        is_inf_time = True
        break

# 출력
# 1번 도시에서 출발해 어떤 도시로 가는 과정에서 시간을 무한히 되돌리면 -1

# answers.sort()
if is_inf_time:
    print(-1)
else:
    for i in range(2, N+1):
        if time_costs[i] == INF:
            print(-1)
        else:
            print(time_costs[i])

# print(time_costs)