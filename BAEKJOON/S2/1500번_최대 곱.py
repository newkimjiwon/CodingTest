def solution(s, k):
    q = s // k  # 몫
    r = s % k   # 나머지

    return (q + 1) ** r * q ** (k - r)


def main():
    s, k = map(int, input().split())
    print(solution(s, k))


if __name__ == "__main__":
    main()