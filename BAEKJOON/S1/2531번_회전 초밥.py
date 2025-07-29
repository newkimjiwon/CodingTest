def solution():
    # 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
    n, d, k, c = map(int, input().split())

    sushi = [int(input()) for _ in range(n)]

    count = 1

    check = [0] * (d + 1)  # 먹었는지 안먹었는지 확인

    check[c] += 1 # 쿠폰은 항상 추가할 수 있다.

    for i in range(k):  # 초기 윈도우 슬라이싱
        if check[sushi[i]] == 0:
            count += 1
        check[sushi[i]] += 1

    max_answer = count

    for i in range(1, n):
        # 왼쪽 윈도우 슬라이싱
        check[sushi[i - 1]] -= 1
        if check[sushi[i - 1]] == 0:
            count -= 1
        
        # 오른쪽 윈도우 슬라이싱
        right = (i + k - 1) % n
        if check[sushi[right]] == 0:
            count += 1
        check[sushi[right]] += 1
        
        max_answer = max(max_answer, count)

    print(max_answer)


if __name__=="__main__":
    solution()