if __name__=="__main__":
    n = int(input())
    k = int(input())

    cards = [input() for _ in range(n)]

    s = set()

    visited = [False] * n

    def dfs(k, count, number):
        if k == count:
            s.add(number)
            return
        
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(k, count + 1, number + cards[i])
                visited[i] = False
    
    dfs(k, 0, '')
    
    print(len(s))