def solution():
    N, M = map(int, input().split())

    balls = [i for i in range(N + 1)]  # 공

    for _ in range(M):
        i, j = map(int, input().split())
        # 교체하는 알고리즘
        i_ball = balls[i]
        balls[i] = balls[j]
        balls[j] = i_ball

    for i in range(1, N + 1):
        print(balls[i], end = ' ')


if __name__=="__main__":
    solution()