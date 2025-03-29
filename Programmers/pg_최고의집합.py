'''
https://school.programmers.co.kr/learn/courses/30/lessons/12938

자연수 n 개로 이루어진 중복 집합 중 다음 두 조건을 만족하는 집합을 최고의 집합이라고 한다.

1. 각 원소의 합이 S가 되는 수의 집합
2. 위 조건을 만족하면서 각 원소의 곱이 최대가 되는 집합



n = 5
s = 10

2,2,2,2,2 = 32
3,2,2,2,1 = 24
4,2,2,1,1 = 16
5,2,1,1,1 = 10
6,1,1,1,1 = 6

n = 3
s = 11

2,4,4 = 32
3,3,5 = 45
4,2,5 = 40



'''

def solution(n, s):
    answer = [-1]

    div_val = s // n
    if 0 >= div_val:
        return answer

    answer.clear()
    rest_val = 0
    while True:
        if n <= len(answer):
            rest_val = s
            break

        s -= div_val
        answer.append(div_val)

    while True:
        for i in range(len(answer)):
            answer[i] += 1
            rest_val -= 1
            if rest_val <= 0:
                break
        if rest_val <= 0:
            break

    answer.sort() # 오름차순 정렬
    return answer

def val_mul(src):
    ret_val = 1
    for s in src:
        ret_val *= s
    return ret_val

### MAIN ###
if "__main__" == __name__:
    ans_1 = solution(
        2, 9
    )
    print(f"ans_1: {ans_1}")

    ans_2 = solution(
        2, 1
    )
    print(f"ans_2: {ans_2}")

    ans_3 = solution(
        2, 8
    )
    print(f"ans_3: {ans_3}")


    ans_4 = solution(
        3, 11
    )
    print(f"ans_4: {ans_4}, mul: {val_mul(ans_4)}, sum: {sum(ans_4)}")

    ans_5 = solution(
        5, 10
    )
    print(f"ans_5: {ans_5}, mul: {val_mul(ans_5)}, sum: {sum(ans_5)}")

    ans_6 = solution(
        2, 2
    )
    print(f"ans_6: {ans_6}, mul: {val_mul(ans_6)}, sum: {sum(ans_6)}")

    ans_7 = solution(
        2, 3
    )
    print(f"ans_7: {ans_7}, mul: {val_mul(ans_7)}, sum: {sum(ans_7)}")

    ans_8 = solution(
        5, 13
    )
    print(f"ans_8: {ans_8}, mul: {val_mul(ans_8)}, sum: {sum(ans_8)}")