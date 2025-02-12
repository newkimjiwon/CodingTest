# 치킨 거리 최소화를 위한 조합 탐색 함수
# a: 현재 탐색 중인 치킨집의 인덱스
# b: 현재까지 선택한 치킨집 개수
# chicken: 치킨집 위치 리스트
# house: 집 위치 리스트
# val: 현재 선택된 치킨집 인덱스 리스트
# m: 남길 치킨집 개수
def solution(a, b, chicken, house, val, m):
    global distance_min

    # 모든 치킨집을 고려했을 때 종료
    if a > len(chicken):
        return

    # m개의 치킨집을 선택한 경우, 도시의 치킨 거리 계산
    if b == m:
        distance_total = 0  # 전체 치킨 거리
        for r, c in house:
            distance = float('inf')  # 특정 집의 최소 치킨 거리
            for i in val:
                nr, nc = chicken[i]  # 선택된 치킨집 위치
                distance = min(distance, abs(nr - r) + abs(nc - c))  # 최소 거리 갱신
            distance_total += distance  # 전체 거리 합산

        # 현재 조합에서의 최소 치킨 거리 갱신
        distance_min = min(distance_min, distance_total)
        return

    # 현재 치킨집 선택하는 경우 (백트래킹 탐색)
    val.append(a)
    solution(a + 1, b + 1, chicken, house, val, m)
    val.pop()  # 백트래킹 (선택 취소)

    # 현재 치킨집 선택하지 않는 경우
    solution(a + 1, b, chicken, house, val, m)


# 메인 함수
def main():
    global distance_min
    distance_min = float('inf')  # 최소 거리 초기화 (무한대 값 설정)

    # n: 도시 크기 (n x n), m: 유지할 치킨집 개수
    n, m = map(int, input().split())

    # 도시 정보 입력 받기
    city = [list(map(int, input().split())) for _ in range(n)]

    # 치킨집과 집 위치 저장 리스트
    chicken, house, val = [], [], []

    # 도시 정보에서 치킨집과 집의 좌표를 저장
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                house.append((i, j))  # 집 위치 저장
            elif city[i][j] == 2:
                chicken.append((i, j))  # 치킨집 위치 저장

    # 백트래킹을 이용해 m개의 치킨집 조합 중 최소 거리 탐색
    solution(0, 0, chicken, house, val, m)

    # 최소 치킨 거리 출력
    print(distance_min)


# 프로그램 실행 (메인 함수 호출)
if __name__ == "__main__":
    distance_min = 0  # 전역 변수 초기화
    main()