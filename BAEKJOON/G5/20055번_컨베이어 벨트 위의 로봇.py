from collections import deque


def robot(n, k, belt):
    dq = deque(belt)  # 벨트 내구도
    robots = deque([False] * (2 * n))  # 로봇 존재 여부
    step = 0  # 단계 수

    while True:
        step += 1

        # 1. 벨트와 로봇 함께 회전
        dq.rotate(1)
        robots.rotate(1)
        robots[n - 1] = False  # 내리는 위치에 로봇은 무조건 내려감

        # 2. 로봇 이동 (앞에서부터 순차적으로)
        for i in range(n - 2, -1, -1):  # N-2 ~ 0
            if robots[i] and not robots[i + 1] and dq[i + 1] > 0:
                robots[i] = False
                robots[i + 1] = True
                dq[i + 1] -= 1
        robots[n - 1] = False  # 내리는 위치 다시 체크

        # 3. 로봇 올리기
        if dq[0] > 0 and not robots[0]:
            robots[0] = True
            dq[0] -= 1

        # 4. 내구도 0인 칸 개수 세기
        if dq.count(0) >= k:
            return step


def main():
    n, k = map(int, input().split())

    belt = list(map(int, input().split()))

    print(robot(n, k, belt))


if __name__=="__main__":
    main()