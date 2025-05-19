from collections import deque


def main():
    n, k = map(int, input().split())

    q = deque([i for i in range(1, n + 1)])

    count = 1

    result = []

    while q:
        if count == k and len(q) >= 2:
            result.append(str(q.popleft()) + ',')
            count = 1
        elif count == k and len(q) == 1:
            result.append(str(q.popleft()))
        else:
            f = q.popleft()
            q.append(f)
            count += 1

    print('<', end = '')
    print(' '.join(result), end = '')
    print('>')


if __name__=="__main__":
    main()