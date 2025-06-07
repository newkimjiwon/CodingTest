from collections import deque


def solution():
    dq = deque()
    n = int(input())
    result = []

    for _ in range(n):
        command = input().split()

        if command[0] == 'push_front':
            dq.appendleft(int(command[1]))
        elif command[0] == 'push_back':
            dq.append(int(command[1]))
        elif command[0] == 'pop_front':
            if dq:
                result.append(dq.popleft())
            else:
                result.append(-1)
        elif command[0] == 'pop_back':
            if dq:
                result.append(dq.pop())
            else:
                result.append(-1)
        elif command[0] == 'size':
            result.append(len(dq))
        elif command[0] == 'empty':
            result.append(0 if dq else 1)
        elif command[0] == 'front':
            result.append(dq[0] if dq else -1)
        elif command[0] == 'back':
            result.append(dq[-1] if dq else -1)

    for i in result:
        print(i)


if __name__ == "__main__":
    solution()