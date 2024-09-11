# N은 숫자가 나올 수 있는 최대, M은 수열의 길이
N, M = map(int, input().split())
line = list(map(int, input().split()))

line.sort()  # 숫자들을 정렬합니다.

answer = []
used = [False] * N  # 각 숫자가 사용되었는지를 추적하기 위한 리스트

def dfs():
    if len(answer) == M:  # 수열의 길이가 M에 도달하면 출력
        print(' '.join(map(str, answer)))
        return

    for i in range(N):
        if not used[i]:  # i번째 숫자가 사용되지 않았으면
            used[i] = True  # 현재 숫자를 사용한 것으로 표시
            answer.append(line[i])  # 수열에 숫자를 추가
            dfs()  # 재귀 호출
            answer.pop()  # 재귀가 끝나면 숫자를 다시 제거 (백트래킹)
            used[i] = False  # 숫자를 사용하지 않은 상태로 돌려놓음

dfs()