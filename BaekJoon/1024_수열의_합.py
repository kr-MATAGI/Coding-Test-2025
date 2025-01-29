'''
    N과 L이 주어질 때,
    합이 N이면서
    길이가 적어도 L인 가장 짧은 연속된 음이 아닌 정수 리스트를 구하는 프로그램

    1)
        18  2

    2)
        18  4


    3)  여기서 어떻게 해결할지 봐야됨
        1000000000  2


        n + (n+1) + (n+2) + (n+3) + (n+4) ... (n+m) = 1,000,000,000
        2n + 1 = 1,000,000,000
        3n + 3 = 1,000,000,000
            3n = 999,999,997
        4n + 6 = 1,000,000,000
            4n = 999,999,994
        5n + 10 = 1,000,000,000
            5n = 999,999,990
            n = 199,999,998 -> n 만큼
            199,999,998 + 199,999,999 + 200,000,000 + 200,000,0001, 200,000,002

    4)
        45  10

        10n + 55
        n
        n+1
        n+2
        n+3
        n+4
        n+5
        n+6
        n+7
        n+8
        n+9
        10n + 45 = 45
            n = 0
            
    5) 18   5
        n
        n+1
        n+2
        n+3
        n+4
        5n+10 = 18
        5n = 8
        n = 1.6

        n+5
        6n+15 = 18

        
'''
N, L = map(int, input().split())

'''
    계산 방식 결론
        n + (n+1) + (n+2) + (n+3) ... = N 공식 사용
        -> 단순 공식만으로 시간 초과 발생 (83%?)
        -> 계산이 불가능한 판단에서 시간초과 발생했었음
'''
store_n = L
store_m = sum([i for i in range(0, L)])
answer = -1

copy_n = N
while True:
    # print(f"{store_n}n + {store_m} = {(copy_n - store_m) // store_n}")
    if 0 > (copy_n - store_m) // store_n:
        break

    if (
        0 != (copy_n - store_m) % store_n 
        or store_n < L
    ):
        # 자연수가 아님 or 요구하는 수열 길이보다 작음
        store_m += store_n
        store_n += 1        
        continue

    calc_res = (copy_n - store_m) // store_n
    # 음의 정수 리스트가 구해짐
    if 0 > calc_res:
        break

    num_list = [calc_res]
    for i in range(1, store_n):
        num_list.append(calc_res + i)
    
    # 길이가 100보다 큼
    if 100 < len(num_list):
        break

    answer = num_list
    break

if -1 == answer:
    print(answer)
else:
    print(" ".join([str(x) for x in answer]))