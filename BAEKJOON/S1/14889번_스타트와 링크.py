from itertools import combinations


def solution():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    min_diff = int(1e9)

    # 가능한 팀 조합 절반만 순회
    people = list(range(n))
    for team1 in combinations(people, n // 2):
        team2 = list(set(people) - set(team1))

        # 팀 능력치 계산
        def team_score(team):
            score = 0
            for i in team:
                for j in team:
                    if i != j:
                        score += arr[i][j]
            return score

        diff = abs(team_score(team1) - team_score(team2))
        min_diff = min(min_diff, diff)

        if min_diff == 0:
            break  # 최적값 조기 종료

    print(min_diff)


if __name__=="__main__":
    solution()