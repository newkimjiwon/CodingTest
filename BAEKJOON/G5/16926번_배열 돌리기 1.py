import sys
input = sys.stdin.readline


def rotate_layers(arr, N, M, R):
    layers = min(N, M) // 2
    for s in range(layers):
        top, left = s, s
        bottom, right = N - 1 - s, M - 1 - s

        ring = []
        # 위쪽 줄 (왼→오, right는 직전까지)
        for x in range(left, right):
            ring.append(arr[top][x])
        # 오른쪽 줄 (위→아래, bottom 직전까지)
        for y in range(top, bottom):
            ring.append(arr[y][right])
        # 아래쪽 줄 (오→왼, left 다음까지)
        for x in range(right, left, -1):
            ring.append(arr[bottom][x])
        # 왼쪽 줄 (아래→위, top 다음까지)
        for y in range(bottom, top, -1):
            ring.append(arr[y][left])

        L = len(ring)
        k = R % L
        if k:
            ring = ring[k:] + ring[:k]  # 반시계 방향 회전

        idx = 0
        # 다시 채워넣기 (순서 동일)
        for x in range(left, right):
            arr[top][x] = ring[idx]; idx += 1
        for y in range(top, bottom):
            arr[y][right] = ring[idx]; idx += 1
        for x in range(right, left, -1):
            arr[bottom][x] = ring[idx]; idx += 1
        for y in range(bottom, top, -1):
            arr[y][left] = ring[idx]; idx += 1


if __name__ == "__main__":
    N, M, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rotate_layers(arr, N, M, R)

    out_lines = []
    for row in arr:
        out_lines.append(' '.join(map(str, row)))
    print('\n'.join(out_lines))