R, C = map(int, input().split())
# 목장 초깃값
pasture = []
# 목장 추가
for _ in range(R):
    line = list(input())
    pasture.append(line)

def solution(pasture):
    # 양 기준으로 좌우 방향 살펴보기
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i in range(len(pasture)):
        for j in range(len(pasture[i])):
            # 울타리의 최소 개수를 구하는 문제가 아니므로 그냥 양이랑 늑대 제외 울타리 다 설치
            if pasture[i][j] == '.':
                pasture[i][j] = 'D'
            # 양이 나오면 좌우에 늑대가 있는지 살펴봄 있으면 0 리턴
            elif pasture[i][j] == 'S':
                for ny, nx in move:
                    y = i + ny
                    x = j + nx
                    if 0 <= y < len(pasture) and 0 <= x < len(pasture[i]) and pasture[y][x] == 'W':
                        return 0
    # 반복문이 끝나면 자동으로 늑대가 없다는 결 확인 후 1 리턴
    return 1

# 결과 값 출력
if solution(pasture) == 1:
    print(1)
    for iy in pasture:
        for ix in iy:
            print(ix, end = "")
        print()
else:
    print(0)