from collections import deque

#  선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다.
#  AC는 정수 배열에 연산을 하기 위해 만든 언어이다.
#  이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.
def ac(current_function, n, arr):
    reverse_flag = False  # 뒤집기 여부를 저장하는 플래그
    dq = deque(arr)

    for p in current_function:
        if p == 'R':
            reverse_flag = not reverse_flag  # 뒤집기 여부만 토글
        elif p == 'D':
            if dq:
                if reverse_flag:
                    dq.pop()  # 뒤집힌 상태라면 오른쪽에서 제거
                else:
                    dq.popleft()  # 정방향이라면 왼쪽에서 제거
            else:
                return 'error'  # 빈 deque에서 제거 시도 시 에러

    # 플래그에 따라 결과를 결정
    if reverse_flag:
        dq.reverse()

    # 결과 문자열 생성
    return '[' + ','.join(map(str, dq)) + ']'


def main():
    t = int(input())  # 테스트 케이스 개수
    result = []

    for _ in range(t):
        p = list(input())  # 수행할 함수 p
        n = int(input())  # 배열에 들어있는 수의 개수 n

        # 배열에 들어갈 숫자들 처리
        arr_input = input().strip("[]").strip()
        arr = list(map(int, arr_input.split(","))) if arr_input else []

        result.append(ac(p, n, arr))

    # 결과 값 출력
    for res in result:
        print(res)

main()