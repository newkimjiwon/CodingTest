import sys

def solve_continuous_sum(N):
    start = 1
    end = 1
    current_sum = 1
    count = 0
    
    # end 포인터는 N까지만 이동하며 탐색
    while end <= N:
        
        # Case 1: 합이 N과 같을 때 (정답)
        if current_sum == N:
            count += 1
            
            # 다음 수열 탐색을 위해 start 윈도우 축소/이동
            current_sum -= start
            start += 1
            
            # end 윈도우 확장
            end += 1
            if end <= N:
                current_sum += end
                
        # Case 2: 합이 N보다 작을 때 (합을 키워야 함)
        elif current_sum < N:
            # end를 증가시켜 윈도우 확장
            end += 1
            if end <= N:
                current_sum += end
                
        # Case 3: 합이 N보다 클 때 (합을 줄여야 함)
        else: # current_sum > N
            # start 값을 빼고 start를 증가시켜 윈도우 축소
            current_sum -= start
            start += 1
            
    return count


if __name__=="__main__":
    N = int(sys.stdin.readline())

    result = solve_continuous_sum(N)
    print(result)