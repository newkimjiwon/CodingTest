def bfs(n, m, friend):
    answer = 0

    friend_to_friend = []

    visited = [False] * (n + 1)
    visited[1] = True

    # 1번의 친구부터 조사
    for i in friend[1]:
        if not visited[i]:
            answer += 1
            friend_to_friend.append(i)
            visited[i] = True
    
    # 친구의 친구 조사
    for i in friend_to_friend:
        for ii in friend[i]:
            if not visited[ii]:
                answer += 1
                visited[ii] = True

    return answer


if __name__=="__main__":
    n = int(input())
    m = int(input())
    friends = {i : [] for i in range(1, n + 1)}

    for _ in range(m):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)

    print(bfs(n, m, friends))