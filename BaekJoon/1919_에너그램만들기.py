'''
    두 영단어의 철자 순서를 뒤바꾸어 같아질 수 있을 때, 두 단어를 에너그램이라고 할 수 있다.

    두 개의 영어 단어가 주어졌을 때,
    에너그램의 관계를 만들기 위해 최소한 제거해야하는 에너그램의 개수

    1) 
        dared -> d 제거 -> ared
        bread -> b 제거 -> read

    * 풀이방법
        - 각 단어의 알파벳 배열 생성
        - 배열의 숫자가 큰 곳을 하나씩 제거
'''

import sys

inp_word_1 = str(sys.stdin.readline().strip())
inp_word_2 = str(sys.stdin.readline().strip())

min_alpha = ord('a') - ord('a')
max_alpha = ord('z') - ord('a') + 2
word_1_arr = [0 for _ in range(min_alpha, max_alpha)]
word_2_arr = [0 for _ in range(min_alpha, max_alpha)]

# 배열 셋팅
inp_word_1 = list(inp_word_1)
inp_word_2 = list(inp_word_2)

minus_val = ord('a')
for char in inp_word_1:
    char2int = (ord(char.lower()) - minus_val)
    word_1_arr[char2int] += 1

for char in inp_word_2:
    char2int = (ord(char.lower()) - minus_val)
    word_2_arr[char2int] += 1

# 계산
answer = 0
for i in range(min_alpha, max_alpha):
    if word_1_arr[i] == word_2_arr[i]:
        # 삭제할 필요 없음
        continue
    elif word_1_arr[i] > word_2_arr[i]:
        answer += word_1_arr[i] - word_2_arr[i]
        word_1_arr[i] = word_2_arr[i]
    else:
        answer += word_2_arr[i] - word_1_arr[i]
        word_2_arr[i] = word_1_arr[i]

print(answer)