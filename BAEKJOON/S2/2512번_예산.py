def solution(n, arr, limit):
    # 다 더해도 총 예산보다 작을 때
    if sum(arr) <= limit:
        return max(arr)
    
    right = max(arr)  # 가장 큰 값
    left = 1  # 가장 작은 값

    answer = 0  # 결과

    while left <= right: 
        center = (left + right) // 2 # 중간 값

        result = 0

        for i in arr:
            if i <= center:  # 작으면 크기 만큼
                result += i
            else:  # 크면 평균 값 만큼
                result += center 
        
        if result <= limit:
            answer = center
            left = center + 1
        else:
            right = center - 1

    return answer

if __name__=="__main__":
    n = int(input())
    g = list(map(int, input().split()))
    l = int(input())
    print(solution(n, g, l))
    
    # print(solution(4, [120, 110, 140, 150], 485))