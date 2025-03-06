def dfs(current, n, m, sequence, start):
    if len(current) == m:
        print(' '.join(current))
        return

    for i in range(start, n):
        current.append(str(sequence[i]))   # 1, 1과 같은 중복 원소 사용을 허용한다.
        dfs(current, n, m, sequence, i)  # 다음 상태로 이동
        current.pop()  # 중복되는 수열 방지


if __name__=="__main__":
    n, m = map(int, input().split())

    sequence = list(map(int, input().split()))  # 수열

    sequence.sort()  # 오름차순으로 정렬

    dfs([], n, m, sequence, 0)  # DFS 시작