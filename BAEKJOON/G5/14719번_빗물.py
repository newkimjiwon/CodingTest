def main():
    h, w = map(int, input().split())
    block = list(map(int, input().split()))

    answer = 0  # 정답

    for i in range(1, w - 1):
        left = max(block[:i])  # 좌측 비교
        right = max(block[i + 1:])  # 우측 비교
        m = min(left, right)  # 더 낮은거 선택
        if m > block[i]:  # 낮지만 현재 블록 보다 높아야 물이 쌓임
            answer += m - block[i]

    print(answer)

main()