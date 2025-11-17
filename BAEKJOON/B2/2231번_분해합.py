def solution(N):
    answer = 0
    
    for i in range(1, N):
        tmp = 0
        arr = list(str(i))
        
        for j in arr:
            tmp += int(j)
        
        tmp += i
        
        if tmp == N:
            answer = i
            break
    
    return answer


if __name__=="__main__":
    N = int(input())
    
    print(solution(N)) 