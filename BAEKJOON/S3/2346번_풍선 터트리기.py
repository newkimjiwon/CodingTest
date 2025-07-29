from collections import deque


def solution():
    n = int(input())  # 풍선의 개수

    balloons = deque(list(map(int, input().split())))  # 풍선 deque
    sequense = deque([i for i in range(1, n + 1)])   # 순서

    answer = [1]  # 결과 값 풍선은 무조건 1번부터 터짐

    number = balloons.popleft()
    current = sequense.popleft()

    while balloons:
        if number > 0:
            for _ in range(number - 1):
                next_b = balloons.popleft()
                balloons.append(next_b)
                next_c = sequense.popleft()
                sequense.append(next_c)
            number = balloons.popleft()
            current = sequense.popleft()
        else:
            for _ in range(-number - 1):
                next_b = balloons.pop()
                balloons.appendleft(next_b)
                next_c = sequense.pop()
                sequense.appendleft(next_c)
            number = balloons.pop()
            current = sequense.pop()
        
        answer.append(current)

    for i in answer:
        print(i, end = ' ')


if __name__=="__main__":
    solution()