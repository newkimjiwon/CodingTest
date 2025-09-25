if __name__=="__main__":
    R, C = map(int, input().split())

    move = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 움직임

    islands = [list(input()) for _ in range(R)]

    visited = [[False] * C for _ in range(R)]  # 사라질 섬

    # 바다로 변할 섬 있는지 체크
    for iy in range(R):
        for ix in range(C):
            if islands[iy][ix] == 'X':
                sea = 0  # 바다
                for dy, dx in move:
                    y = iy + dy
                    x = ix + dx
                    # 경계면이 바다인지 확인
                    if 0 <= y < R and 0 <= x < C and islands[y][x] == '.':
                        sea += 1  # 바다
                    # 경계면이 밖으로 벗어나도 바다
                    elif 0 > y or y >= R or 0 > x or x >= C:
                        sea += 1  
                if sea >= 3:
                    visited[iy][ix] = True  # 섬 -> 바다
    
    # 섬 -> 바다
    for iy in range(R):
        for ix in range(C):
            if visited[iy][ix]:
                islands[iy][ix] = '.' 

    top, left = R, C
    bottom, right = 0, 0

    # 좌표 찾기
    for iy in range(R):
        for ix in range(C):
            if islands[iy][ix] == 'X':
                if top > iy:
                    top = iy
                if bottom < iy:
                    bottom = iy
                if left > ix:
                    left = ix
                if right < ix:
                    right = ix
    
    for ay in range(top, bottom + 1):
        for ax in range(left, right + 1):        
            print(islands[ay][ax], end = '')
        print()