def solution(N, A):
    # prefix XOR 생성 (0 포함)
    prefix = [0]
    cur = 0
    for x in A:
        cur ^= x
        prefix.append(cur)

    answer = 0

    # 0~31비트까지 확인
    for bit in range(32):
        zero = 0
        one = 0

        for p in prefix:
            if (p >> bit) & 1:
                one += 1
            else:
                zero += 1

        answer += zero * one * (1 << bit)

    return answer


if __name__=="__main__":
    N = int(input())
    A = list(map(int, input().split()))  # 배열

    print(solution(N, A))