def factorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans


def solution(n, m):
    return factorial(n) // (factorial(n - m) * factorial(m))


if __name__=="__main__":
    n, m = map(int, input().split())
    print(solution(n, m))