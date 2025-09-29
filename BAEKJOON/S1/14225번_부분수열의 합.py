if __name__=="__main__":
    N = int(input())
    S = list(map(int, input().split()))

    # 중복처리
    duplicate = set()

    def dfs(start, l, count, value):
        if count == l:
            duplicate.add(value)
            return
        
        for i in range(start, N):
            dfs(i + 1, l, count + 1, value + S[i])
    
    for i in range(1, N + 1):
        dfs(0, i, 0, 0)

    # 가능한 합은 최대 sum(S)
    total = sum(S)
    for i in range(1, total+2):
        if i not in duplicate:
            print(i)
            break

"""
# 그리디
if __name__=="__main__":
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()

    target = 1
    for x in S:
        if x <= target:
            target += x
        else:
            break
    print(target)

"""