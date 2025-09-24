from collections import deque


def swings(arrs, N, M, R):
    new_arrs = [[0] * M for _ in range(N)]  # 새로운 배열
    min_value = min(N, M) // 2

    for i in range(min_value):
        top, left = i, i
        bottom, right = N - i - 1, M - i - 1

        peri = 0    # 회전 겉 둘래 구하는 법
        arr_peri = deque()

        # 왼쪽  -> 오른쪽
        for x1 in range(left, right):
            arr_peri.append(arrs[top][x1])
            peri += 1
        # 위쪽 -> 아래
        for y1 in range(top, bottom):
            arr_peri.append(arrs[y1][right])
            peri += 1
        # 아래 -> 왼쪽
        for x2 in range(right, left, -1):
            arr_peri.append(arrs[bottom][x2])
            peri += 1
        # 아래 -> 위쪽
        for y2 in range(bottom, top, -1):
            arr_peri.append(arrs[y2][left])
            peri += 1

        # 회전 (둘레만큼 움직이면 다시 되돌아온다)
        for _ in range(R % peri):
            current = arr_peri.popleft()
            arr_peri.append(current)

        # 왼쪽  -> 오른쪽
        for x1 in range(left, right):
            value = arr_peri.popleft()
            new_arrs[top][x1] = value
        # 위쪽 -> 아래
        for y1 in range(top, bottom):
            value = arr_peri.popleft()
            new_arrs[y1][right] = value
        # 아래 -> 왼쪽
        for x2 in range(right, left, -1):
            value = arr_peri.popleft()
            new_arrs[bottom][x2] = value
        # 아래 -> 위쪽
        for y2 in range(bottom, top, -1):
            value = arr_peri.popleft()
            new_arrs[y2][left] = value

    return new_arrs



if __name__=="__main__":
    N, M, R = map(int, input().split())  # N, M과 수행해야 하는 회전의 수 R

    arr = [list(map(int, input().split())) for _ in range(N)]  # 스윙

    arr = swings(arr, N, M, R)

    for i in arr:
        for j in i:
            print(j, end = ' ')
        print()