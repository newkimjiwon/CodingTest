# 알고리즘
# 1. dp 테이블 초기화: dp[i]는 i원을 만드는 모든 방법의 수를 저장한다.
#    0원을 만드는 방법은 '아무 동전도 사용하지 않는 한 가지 방법'이므로 dp[0]을 1로 초기화한다.
# 2. 각 동전 종류를 순회한다. (오름차순 정렬되어 있다면 더욱 효율적일 수 있다.)
#    for coin in coins:
# 3. 현재 동전(coin)을 사용하여 만들 수 있는 금액들을 순회한다.
#    금액은 현재 동전의 값(coin)부터 목표 금액(money)까지 증가시키며 확인한다.
#    for i in range(coin, money + 1):
# 4. 점화식 적용: dp[i]는 현재 금액 i를 만드는 방법의 수이다.
#    이전에 i - coin 원을 만들었던 방법의 수 (dp[i - coin])를 현재 dp[i]에 더한다.
#    이는 현재 동전(coin)을 사용하여 i원을 만드는 새로운 방법의 수를 추가하는 것이다.
#    dp[i] = dp[i] + dp[i - coin]

def dp(n, coins, money):
    dp = [0] * (money + 1)  # money가 되었을 때 동전의 조합 개수를 구한다.

    dp[0] = 1

    for coin in coins:  # 동전의 종류를 출력
        for i in range(coin, money + 1):  # 0원 동전은 존재하지 않는다.
            dp[i] = dp[i] + dp[i - coin]
        
    return dp[money]


def main():
    t = int(input())  # 테스트 케이스의 수

    result = []  # 결과 값

    for _ in range(t):
        n = int(input())  # 동전의 가지 수

        coins = list(map(int, input().split()))  # 코인

        coins.sort()  # 오름차순으로 정렬

        money = int(input())  # 돈

        result.append(dp(n, coins, money))

    for i in result:
        print(i)


if __name__=="__main__":
    main()