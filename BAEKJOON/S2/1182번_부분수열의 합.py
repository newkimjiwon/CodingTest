# 전역변수
count = 0


def dfs(index, current_sum, s, sequence):
    global count

    if index >= len(sequence):
        return

    # 현재 원소를 포함하는 경우
    current_sum += sequence[index]

    if current_sum == s:
        count += 1  # 부분수열의 합이 S이면 카운트 증가

    # 다음 원소 탐색 (현재 원소 포함한 경우)
    dfs(index + 1, current_sum, s, sequence)

    # 현재 원소를 포함하지 않는 경우 (백트래킹)
    dfs(index + 1, current_sum - sequence[index], s, sequence)


def main():
    global count
    n, s = map(int, input().split())  # N, S 입력
    sequence = list(map(int, input().split()))  # 수열 입력

    # DFS 실행
    dfs(0, 0, s, sequence)

    print(count)


main()