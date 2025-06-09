def solution():
    n, m = map(int, input().split())
    
    s = set()  # 문자열 집합 S
    answer = 0

    for _ in range(n):
        word = input().strip()
        s.add(word)

    for _ in range(m):
        word = input().strip()
        if word in s:
            answer += 1

    print(answer)


if __name__ == "__main__":
    solution()