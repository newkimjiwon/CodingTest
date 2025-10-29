# 백준 3015번 - 오아시스 재결합

import sys
input = sys.stdin.readline

def solution(N, people):
    answer = 0  # Result

    stack = []  # Stack

    for n in people:
        count = 1  # 같은 키 사람 수 (초기 1명)
        
        # 스택의 top이 현재 사람보다 작으면 pop하면서 볼 수 있는 쌍 누적
        while stack and stack[-1][0] < n:
            height, c = stack.pop()
            answer += c  # 작은 키 그룹은 모두 볼 수 있음

        # 같은 키가 있을 경우
        if stack and stack[-1][0] == n:
            height, c = stack.pop()
            answer += c  # 같은 키 그룹끼리는 모두 볼 수 있음
            count += c   # 같은 키 사람 수 누적
            if stack:
                answer += 1  # 자기보다 큰 사람이 뒤에 남아 있으면 그 사람도 볼 수 있음
        else:
            if stack:
                answer += 1  # 자기보다 큰 사람 1명은 항상 볼 수 있음

        stack.append((n, count))  # 현재 사람을 스택에 추가

    return answer


if __name__=="__main__":
    N = int(input())  # N명이 한 줄로 서서 기다리고 있다.

    people = [int(input()) for _ in range(N)]  # 사람

    print(solution(N, people))  # 결과