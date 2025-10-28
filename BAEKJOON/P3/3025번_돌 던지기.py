import sys
input = sys.stdin.readline


def falling(x, y, line, arr, checkpoint, R, C):
    """
    돌을 실제로 떨어뜨리는 함수
    (왼쪽/오른쪽 미끄러짐 규칙 포함)
    """
    while True:
        checkpoint[line].append([x, y])  # 현재 경로 저장

        # 1. 바닥 또는 벽이면 현재 위치에 멈춤
        if x + 1 == R or arr[x + 1][y] == "X":
            arr[x][y] = "O"
            return

        # 2. 아래가 돌(O)이라면 미끄러짐 검사
        if arr[x + 1][y] == "O":
            # 왼쪽 아래로 이동 가능하면 왼쪽으로
            if y - 1 >= 0 and arr[x][y - 1] == "." and arr[x + 1][y - 1] == ".":
                y -= 1
            # 오른쪽 아래로 이동 가능하면 오른쪽으로
            elif y + 1 < C and arr[x][y + 1] == "." and arr[x + 1][y + 1] == ".":
                y += 1
            # 둘 다 불가능하면 현재 위치에서 멈춤
            else:
                arr[x][y] = "O"
                return

        # 3. 단순히 아래가 비었으면 계속 내려감
        x += 1


def drop_stone(column, arr, checkpoint, R, C):
    """
    지정한 열(column)에 돌을 떨어뜨림
    - 이전 낙하 경로(checkpoint)가 있으면 그 경로 재활용
    - 없으면 맨 위(0행)에서 시작
    """
    col = column

    # 캐시된 경로가 남아 있다면 유효한 좌표만 남길 것
    while checkpoint[col]:
        cx, cy = checkpoint[col][-1]
        if arr[cx][cy] == '.':
            break
        checkpoint[col].pop()  # 이미 돌이 쌓인 곳은 제거

    # 캐시가 있다면 그 위치에서 다시 낙하
    if checkpoint[col]:
        cx, cy = checkpoint[col].pop()
        falling(cx, cy, col, arr, checkpoint, R, C)
    else:
        # 없으면 처음부터 떨어뜨림
        falling(0, col, col, arr, checkpoint, R, C)

    # 낙하 완료 후, 최종 도착 좌표를 꺼내 'O'로 표시
    cx, cy = checkpoint[col].pop()
    arr[cx][cy] = "O"


def main():
    R, C = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(R)]
    checkpoint = [[] for _ in range(C)]
    N = int(input())

    for _ in range(N):
        col = int(input()) - 1  # 열 인덱스 (0-based)
        drop_stone(col, arr, checkpoint, R, C)

    # 최종 결과 출력
    for row in arr:
        print("".join(row))


if __name__ == "__main__":
    main()
