def solution(N, M, n_arr, m_arr):
    answer = []

    dic = {}

    for n in n_arr:  # MAP을 이용해서 갱신
        dic[n] = True

    for m in m_arr:
        if dic.get(m):
            answer.append(1)
        else:
            answer.append(0)

    return answer


if __name__=="__main__":
    T = int(input())  # 테스트 케이스의 개수

    for _ in range(T):
        N = int(input())
        n_arr = list(map(int, input().split()))
        M = int(input())
        m_arr = list(map(int, input().split()))

        answer = solution(N, M, n_arr, m_arr)

        for i in answer:
            print(i)