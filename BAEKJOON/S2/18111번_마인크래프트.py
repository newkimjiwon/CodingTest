def solve(N, M, B, blocks):
    # 최소 시간과 그때의 높이를 저장할 변수
    min_time = float('inf')
    best_height = -1

    # 1. 필드에서 가장 낮은 높이와 높은 높이를 먼저 찾습니다.
    low_block = 256
    high_block = 0
    for row in blocks:
        for val in row:
            if val < low_block: low_block = val
            if val > high_block: high_block = val

    # 2. 가능한 모든 높이(target)에 대해 브루트 포스 탐색을 합니다.
    # low_block부터 high_block까지만 확인해도 충분합니다.
    for target in range(low_block, high_block + 1):
        install_block = 0  # 채워야 하는 블록 수
        remove_block = 0   # 깎아야 하는 블록 수

        for i in range(N):
            for j in range(M):
                diff = blocks[i][j] - target
                if diff > 0:
                    # 현재 칸이 목표보다 높으면 제거
                    remove_block += diff
                elif diff < 0:
                    # 현재 칸이 목표보다 낮으면 설치
                    install_block -= diff # diff가 음수이므로 빼서 양수로 만듦

        # 3. 작업 가능 여부 확인: (인벤토리 + 깎아서 얻은 블록) >= 채워야 하는 블록
        if remove_block + B >= install_block:
            # 1번 작업(제거)은 2초, 2번 작업(설치)은 1초
            current_time = (remove_block * 2) + install_block
            
            # 4. 최소 시간 갱신
            # 시간이 같다면 '가장 높은 높이'를 출력해야 하므로 <= 조건을 사용합니다.
            if current_time <= min_time:
                min_time = current_time
                best_height = target

    return min_time, best_height


if __name__ == "__main__":   
    N, M, B = map(int, input().split())
    
    blocks = []
    idx = 3
    for _ in range(N):
        blocks.append(list(map(int, input().split())))
        idx += M

    time, height = solve(N, M, B, blocks)
    print(time, height)