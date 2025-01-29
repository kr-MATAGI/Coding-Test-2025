'''
    외계문명의 전파를 수집하여 수집한 전파 속에서 자연적으로 발생하기 힘든 패턴을 찾아냄
    전파의 기본 단위:
        {0, 1}
    x + ()는 최소 x의 반복으로 이루어진 전파의 집합
    (xyx)+ 는 괄호 내의 xyx의 반복으로 이루어짐
    
    + 는 반복을 의미
    | 는 or을 의미


    전파 패턴 (100+1+ | 01)+ 의 패턴을 지니는 전파를 가려내는 프로그램이 필요하다.

    문자열의 길이는 1<=N<=200

    1)
        1001 01 11
    2)
        01 10001 00110001
        
    3)
        01 10001011001
        
    - 작은거부터 매칭
        최소단위가 01, 1001
        100+1+ 는 1001, 10001, 10000001

    * 10% 채점에서 틀렸습니다 발생
        - 예외 케이스 10011
        - 01100

5
10010111
011000100110001
0110001011001
10011
01100
01100000001111111111
100110001
    1001 10001
    10011 0001
1001 1001
10011 1001
'''

# import re
# a = re.match(r"(100+1+|01)+", '10010111') # False
# print(a)
# a = re.match(r"(100+1+|01)+", '011000100110001') # False
# print(a)
# a = re.match(r"(100+1+|01)+", '0110001011001') # True
# print(a)
# a = re.match(r"(100+1+|01)+", '10011') # True
# print(a)
# a = re.match(r"(100+1+|01)+", '01100') # False
# print(a)
# a = re.match(r"(100+1+|01)+", '01100000001111111111') # True
# print(a)

# a = re.match(r"(100+1+|01)+", '100110001') # True
# print(a)
# a = re.match(r"(100+1+|01)+", '10011001') # True
# print(a)
# 100110011101 # True

# exit()

T = int(input()) # Test Case

for t_idx in range(T):
    inp_item = str(input())

    answer = False # NO
    
    while True:
        if not inp_item:
            # 모두 일치
            answer = True
            break
        
        input_len = len(inp_item)
        cnt_0 = 1
        cnt_1 = 1
        cnt_01 = 1

        # 맨 앞은 어차피 100+1+ 아니면 01로 잘려나갈 것임
        concat_01 = '01'
        is_cut_01 = False
        while concat_01 == inp_item[:len(concat_01)]:
            inp_item = inp_item.removeprefix(concat_01)
            is_cut_01 = True
        
        is_cnt_0_cut = False
        concat_100 = '10'
        while '10' + ('0' * cnt_0) == inp_item[:len('10' + ('0' * cnt_0))]:
            is_cnt_0_cut = True
            concat_100 += '0'
            cnt_0 += 1

        is_cut_1 = False
        if is_cnt_0_cut:
            concat_1001 = concat_100
            while concat_1001 + ('1' * cnt_1) == inp_item[:len(concat_1001 + ('1' * cnt_1))]:
                is_cut_1 = True
                concat_1001 += '1'

            is_sub_fix = False
            if is_cut_1 and 1 < cnt_1:
                # 아래와 같은 패턴이 나타나는지 확인
                # 100110011101 -> 1001 10011101
                subfix_item = inp_item[len(concat_1001)-1:]
                

                is_sub_0_cut = False
                sub_100 = '10'
                sub_0_cnt = 1
                sub_1_cnt = 1
                while '10' + ('0' * sub_0_cnt) == subfix_item[:len('10' + ('0' * sub_0_cnt))]:
                    is_sub_0_cut = True
                    sub_100 += '0'
                    sub_0_cnt += 1

                if is_sub_0_cut:
                    sub_1001 = sub_100
                    while sub_1001 + ('1' * sub_1_cnt) == subfix_item[:len(sub_1001 + ('1' * sub_1_cnt))]:
                        is_sub_fix = True
                        sub_1001 += '1'
                        sub_1_cnt += 1
                
            if is_sub_fix:
                concat_1001 = concat_1001.removesuffix('1')
            inp_item = inp_item.removeprefix(concat_1001)

        if not is_cut_1 and not is_cut_01:
            break
        
    print('YES' if answer else 'NO')