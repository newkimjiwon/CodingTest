# 한 줄(가로 또는 세로)에 대해 지나갈 수 있는 길인지 판단
def can_go(line, l):
    n = len(line)
    used = [False] * n  # 경사로가 설치된 위치를 표시하는 배열

    for i in range(n - 1):
        # 높이가 같으면 그대로 진행 가능
        if line[i] == line[i + 1]:
            continue

        # 오르막 경사로: 다음 칸이 더 높고, 현재 위치 기준으로 L칸 뒤를 확인
        elif line[i] + 1 == line[i + 1]:
            for j in range(i, i - l, -1):  # 뒤쪽에서부터 L칸 체크
                if j < 0 or line[j] != line[i] or used[j]:
                    return False  # 범위 벗어나거나 높이 다르거나 이미 경사로 있음
                used[j] = True  # 경사로 설치

        # 내리막 경사로: 다음 칸이 더 낮고, 다음 위치 기준으로 L칸 앞으로 확인
        elif line[i] - 1 == line[i + 1]:
            for j in range(i + 1, i + l + 1):  # 앞쪽에서부터 L칸 체크
                if j >= n or line[j] != line[i + 1] or used[j]:
                    return False  # 범위 벗어나거나 높이 다르거나 이미 경사로 있음
                used[j] = True  # 경사로 설치

        # 높이 차가 2 이상이면 경사로 설치 불가
        else:
            return False

    return True  # 전체를 통과했다면 유효한 경로


# 전체 지도에서 지나갈 수 있는 길의 수를 계산
def solution(n, l, maps):
    answer = 0

    # 행(가로) 기준으로 검사
    for i in range(n):
        if can_go(maps[i], l):
            answer += 1

    # 열(세로) 기준으로 검사: 세로줄을 따로 리스트로 구성
    for i in range(n):
        column = [maps[j][i] for j in range(n)]
        if can_go(column, l):
            answer += 1

    return answer


def main():
    # 입력: 지도 크기 n, 경사로 길이 l
    n, l = map(int, input().split())

    # 지도 정보 입력 받기 (n줄)
    maps = [list(map(int, input().split())) for _ in range(n)]

    # 결과 출력
    print(solution(n, l, maps))


if __name__ == "__main__":
    main()