def main():
    n = int(input())

    arr = [str(i) for i in range(1, n + 1)]
    visited = [False] * n

    def dfs(visited, result):
        if len(result) == n:
            print(' '.join(result))
            return
        
        for i in range(n):
            if not visited[i]:
                result.append(arr[i])
                visited[i] = True
                dfs(visited, result)
                result.pop()
                visited[i] = False
    
    dfs(visited, [])


if __name__=="__main__":
    main()