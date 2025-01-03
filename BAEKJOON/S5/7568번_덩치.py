def solution(s):
    # 결과
    result = []
    # 길이
    len_s = len(s)

    for i in range(len_s):
        # 스코어
        score = 1
        # 현재 당사자의 몸무게, 키
        current_weight, current_height = s[i]
        for j in range(len_s):
            d_weight, d_height = s[j]
            # 자신이 아닌 다른 후보가 나와야함
            if i != j:
                # 몸무게, 키가 현재의 사람보다 다 크면 낮은 순위로 간다.
                if d_weight > current_weight and d_height > current_height:
                    score += 1
        result.append(score)

    # 결과 값을 출력
    for i in result:
        print(i, end = ' ')

if __name__ == "__main__":
    # 전체 사람의 수 n개 주입
    n = int(input())

    # 사람들 개수 구하기
    people = []

    for _ in range(n):
        weight, height = map(int, input().split())
        people.append([weight, height])

    solution(people)