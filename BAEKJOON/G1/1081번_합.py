import sys
sys.setrecursionlimit(10**6)

def digit_sum(n):
    if n < 0:
        return 0

    digits = list(map(int, str(n)))
    length = len(digits)
    
    dp = [[[-1] * 2 for _ in range(10 * length)] for _ in range(length)]

    def dfs(pos, sum, tight):
        if pos == length:
            return sum

        if dp[pos][sum][tight] != -1:
            return dp[pos][sum][tight]

        limit = digits[pos] if tight else 9
        result = 0

        for digit in range(0, limit + 1):
            result += dfs(pos + 1, sum + digit, tight and (digit == limit))
        
        dp[pos][sum][tight] = result
        return result

    return dfs(0, 0, 1)

def sum_of_digits_in_range(L, U):
    return digit_sum(U) - digit_sum(L - 1)

L, U = map(int, input().split())
print(sum_of_digits_in_range(L, U))