move = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상 하 좌 우 움직임


# 4방향으로 부딪치는지 확인하는 함수
def search(ty, tx, arr):
    for dy, dx in move:
        cy, cx = ty, tx
        while True:
            cy += dy
            cx += dx
            if cy < 0 or cy >= len(arr) or cx < 0 or cx >= len(arr):
                break
            if arr[cy][cx] == 'O':  # 벽
                break
            if arr[cy][cx] == 'S':  # 학생 발견
                return True
    return False  # 모든 방향에서 학생 없음


def solution(arr, N):
    answer = ["NO"]
    t_location = []

    # 선생님 위치 확인
    for iy in range(N):
        for ix in range(N):
            if arr[iy][ix] == 'T':
                t_location.append((iy, ix))

    def wall(count):
        if count == 3:
            for ty, tx in t_location:
                if search(ty, tx, arr):
                    return
            answer[0] = "YES"
            return
        
        for iy in range(N):
            for ix in range(N):
                if arr[iy][ix] == 'X':
                    arr[iy][ix] = 'O'
                    wall(count + 1)
                    arr[iy][ix] = 'X'
                    if answer[0] == 'YES':
                        return

    wall(0)
    return answer[0]


if __name__=="__main__":
    N = int(input())
    school = [list(map(str, input().split())) for _ in range(N)]

    print(solution(school, N))
    """
    print(solution([['X', 'S', 'X', 'X', 'T'],
                    ['T', 'X', 'S', 'X', 'X'],
                    ['X', 'X', 'X', 'X', 'X'],
                    ['X', 'T', 'X', 'X', 'X'],
                    ['X', 'X', 'T', 'X', 'X']], 5))
    """