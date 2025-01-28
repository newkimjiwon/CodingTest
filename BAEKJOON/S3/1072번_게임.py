if __name__=="__main__":
    x, y = map(int, input().split())

    # 현재 승률 계산
    winning_rate = y * 100 // x

    # 이미 승률이 100%인 경우 더 이상 개선 불가
    if winning_rate >= 99:  # 100% 승률이 사실상 불가능하므로 99로 제한
        print(-1)
    else:
        left, right = 1, x  # 이진 탐색 범위 설정
        answer = -1
        
        while left <= right:
            mid = (left + right) // 2  # 중간값 계산
            new_winning_rate = (y + mid) * 100 // (x + mid)
            
            if new_winning_rate > winning_rate:
                answer = mid
                right = mid - 1  # 더 작은 범위 탐색
            else:
                left = mid + 1  # 더 큰 범위 탐색
        
        print(answer)