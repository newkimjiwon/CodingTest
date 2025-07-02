def main():
    n, m = map(int, input().split())  # n = 스크린 크기, m = 바구니 크기
    j = int(input())                  # 사과 개수

    apples = [int(input()) for _ in range(j)]  # 사과 위치 리스트

    answer = 0      # 총 이동 거리
    location = 1    # 바구니 시작 위치 (왼쪽 끝 기준)

    for apple in apples:
        left = location
        right = location + m - 1

        if apple < left:
            # 왼쪽으로 이동
            move = left - apple
            answer += move
            location -= move
        elif apple > right:
            # 오른쪽으로 이동
            move = apple - right
            answer += move
            location += move
        # else: 바구니 안에 있음 → 움직일 필요 없음

    print(answer)


if __name__ == "__main__":
    main()