def solution(line):
    # DP 선언
    p = [0] * (len(line) + 1)
    p[0] = line[0]

    # 바텀-업 방식으로 진행
    for i in range(1, len(line)):
        p[i] = line[i] + p[i - 1]
    
    return sum(p)

# 인원 수를 받는 변수
n = int(input())
# 사람들 줄
people = list(map(int, input().split()))

# 오름차순으로 정렬을 해야 한다.
people.sort()

print(solution(people))