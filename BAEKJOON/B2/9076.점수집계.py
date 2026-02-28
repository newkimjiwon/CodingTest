def main():
    # 테스트 케이스 개수 T 입력
    T = int(input())

    for _ in range(T):
        # 5명의 심판 점수 입력 및 정렬
        scores = list(map(int, input().split()))
        scores.sort()

        # 최고점(scores[4])과 최저점(scores[0])을 제외한 중간 3명 점수
        # 그 중 최고점(scores[3])과 최저점(scores[1])의 차이가 4점 이상인지 확인
        if scores[3] - scores[1] >= 4:
            print("KIN")
        else:
            # 4점 미만이면 중간 3개 점수의 합 출력
            print(sum(scores[1:4]))

if __name__ == "__main__":
    main()