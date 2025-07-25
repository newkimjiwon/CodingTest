def main():
    answer = 0

    t = int(input())  # 합

    n = int(input())  # a len 길이
    a = list(map(int, input().split()))  # 배열 a

    m = int(input())  # b len 길이
    b = list(map(int, input().split()))  # 배열 b

    # A 배열의 모든 부배열 합을 저장할 리스트
    sums_a = []
    # B 배열의 모든 부배열 합을 저장할 리스트
    sums_b = []

    # A 배열 처리
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += a[j]
            sums_a.append(current_sum)

    # B 배열 처리 (A와 동일한 방식)
    for i in range(m):
        current_sum = 0
        for j in range(i, m):
            current_sum += b[j]
            sums_b.append(current_sum)

    # 방법 1: 직접 딕셔너리 만들기
    count_a = {}
    for s in sums_a:
        if s in count_a:
            count_a[s] += 1
        else:
            count_a[s] = 1

    # B의 부배열 합 리스트를 하나씩 확인
    for s_b in sums_b:
        # 필요한 A의 부배열 합(target)을 계산
        target = t - s_b
        
        # target 값이 A의 합 딕셔너리에 있다면,
        # 그 개수(count_a[target])만큼 정답에 더해줌
        if target in count_a:
            answer += count_a[target]

    print(answer)


if __name__=="__main__":
    main()