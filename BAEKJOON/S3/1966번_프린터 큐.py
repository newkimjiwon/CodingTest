from collections import deque


def solution(arr, l):
    answer = 0

    q = deque(arr)

    arr.sort()

    while q:
        current = q.popleft()

        if current == arr[-1]:
            answer += 1  # 작업이 끝났을 때 +1를 해야한다.
            arr.pop() # 작업 끝난 제거
            if l == 0: # 끝난 작업이 목표 작업이면 answer 반환
                return answer
            else:  # 아니면 다시 당긴다
                l -= 1
        else:
            q.append(current)
            l -= 1
            if l < 0:
                l = len(q) - 1


def main():
    n = int(input())  # 문서의 개수

    result = []  # 결과

    for _ in range(n):
        m, l = map(int, input().split())
        arr = list(map(int, input().split()))
        result.append(solution(arr, l))

    for i in result:
        print(i)


main()