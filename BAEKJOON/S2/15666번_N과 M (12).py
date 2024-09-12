n, m = map(int, input().split())

line = list(map(int, input().split()))
line.sort()

result = []

def dfs(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    prev = -1  # 이전에 사용한 숫자를 저장
    for i in range(start, n):
        if prev != line[i]:  # 중복된 수를 건너뜀
            result.append(line[i])
            dfs(i)  # i부터 다시 시작하여 중복 선택 허용
            result.pop()
            prev = line[i]  # 이전 숫자 업데이트

dfs(0)