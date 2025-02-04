
func_1_call = 0
def function_1(a):
    global func_1_call

    if 1 == a or 2 == a:
        func_1_call += 1
        return 1
    
    return function_1(a - 1) + function_1(a - 2)

func_2_call = 0
dp = [0 for _ in range(41)]
def function_2(b):
    global func_2_call

    
    dp[1] = 1
    dp[2] = 1

    if 1 == b or 2 == b:
        return dp[b]

    for idx in range(3, b+1, 1):
        func_2_call += 1
        # print(idx, func_2_call)
        dp[idx] = dp[idx-1] + dp[idx-2]
    
    return dp[b]

N = int(input().strip())
# function_1(N) # 이거 파이썬 시간 초과 발생 ㅋㅋ
function_2(N)
func_1_call_time_limit_solved = sum(dp[:N-1]) + 1

print(f"{func_1_call_time_limit_solved} {func_2_call}")