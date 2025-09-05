answer = 0

def dfs(n, k, working, count, visited, current):
    if count == n:
        global answer
        answer += 1
        return
    
    for i in range(n):
        if not visited[i]:
            if current + working[i] - k < 500:
                continue
            
            visited[i] = True
            dfs(n, k, working, count + 1, visited, current + working[i] - k)
            visited[i] = False
    

if __name__=="__main__":
    n, k = map(int, input().split())
    works = list(map(int, input().split()))
    visited = [False] * n

    dfs(n, k, works, 0, visited, 500)

    print(answer)