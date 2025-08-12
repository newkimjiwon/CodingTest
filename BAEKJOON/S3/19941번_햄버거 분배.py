def solution(ham, n, k):
    answer = 0

    ham = list(ham)

    visited = [False] * n

    for i in range(n):
        if visited[i]:  # 이미 먹은 경우 pass
            continue
        current = ham[i] # 현재
        # 먹을 수 있는지 확인
        for ii in range(i + 1, i + k + 1):
            if ii < n and ham[ii] != current and not visited[ii]:
                answer += 1
                visited[ii] = True
                break

    return answer


if __name__=="__main__":
    n, k = map(int, input().split())
    ham = input()  # 햄버거 리스트
    print(solution(ham, n ,k))

    # print(solution("HHPHPPHHPPHPPPHPHPHP", 20 , 1))