def solution(arr):
    answer = 0
    prefix_sum = 0

    # 나머지를 저장할 리스트 (최대 나머지는 m-1까지 가능하므로 크기는 m)
    mod_count = [0] * m

    # 처음에 나머지가 0인 구간을 카운트하기 위해 0을 미리 설정
    mod_count[0] = 1

    for num in arr:
        prefix_sum += num
        mod = prefix_sum % m

        # 나머지가 음수일 경우를 대비 (파이썬에서 %는 음수 나머지를 반환할 수 있음)
        if mod < 0:
            mod += m

        # 나머지가 같은 경우를 카운트
        answer += mod_count[mod]

        # 나머지를 카운트에 추가
        mod_count[mod] += 1

    return answer


# 입력 받기
n, m = map(int, input().split())
result = list(map(int, input().split()))

# 결과 출력
print(solution(result))