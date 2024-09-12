N = int(input())

def factorial(n):
    # 동적 계획법을 위한 테이블 초기화
    dp = [1] * (n + 1)

    # 팩토리얼 계산, 뒤의 0을 줄이기 위해 각 단계에서 10의 배수를 줄여 나간다.
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] * i
        while dp[i] % 10 == 0:
            dp[i] //= 10
        dp[i] %= 100000000000000000  # 뒤 0이 아닌 숫자를 추적하기 위해 필요한 자리수만 유지

    return dp[n]


number = str(factorial(N))
five = []
d = 0

# 뒤에서부터 0이 아닌 5자리를 찾기
for i in range(len(number) - 1, -1, -1):
    if d == 0 and number[i] == '0':
        continue
    elif d == 0 and number[i] != '0':
        d = 1
        five.append(number[i])
    elif d == 1:
        five.append(number[i])
    if len(five) == 5:
        break

# 결과를 역순으로 출력
print("".join(five[::-1]))
