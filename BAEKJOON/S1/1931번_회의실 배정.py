def solution(m):
    count = 0

    # end는 현재 회의 끝나는 시간
    end = -1

    # s는 다음 회의 시작, e는 다음 회의 끝
    for s, e in m:
        if end <= s:
            count += 1
            end = e

    return count

N = int(input())

meeting = []

for _ in range(N):
    # i, j = 회의 시작 시간, 회의 끝나는 시간
    i, j = map(int, input().split())
    meeting.append([i, j])

meeting.sort(key = lambda x: (x[1], x[0]))

print(solution(meeting))