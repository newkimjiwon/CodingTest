def solution(n, sequence, sign_word):
    max_value = -int(1e9)
    min_value = int(1e9)
    used = [False] * len(sign_word)
    numbers = sequence

    def dfs(count, current_result):
        nonlocal max_value, min_value

        if count == n - 1:
            max_value = max(max_value, current_result)
            min_value = min(min_value, current_result)
            return

        visited_operators = set()  # 이번 단계에서 이미 사용한 연산자 기호 방지

        for i in range(len(sign_word)):
            if not used[i] and sign_word[i] not in visited_operators:
                used[i] = True
                visited_operators.add(sign_word[i])  # 같은 연산자 중복 방지

                num = numbers[count + 1]
                new_result = current_result

                if sign_word[i] == '+':
                    new_result += num
                elif sign_word[i] == '-':
                    new_result -= num
                elif sign_word[i] == '*':
                    new_result *= num
                elif sign_word[i] == '/':
                    if new_result < 0:
                        new_result = -(-new_result // num)
                    else:
                        new_result //= num

                dfs(count + 1, new_result)
                used[i] = False

    dfs(0, numbers[0])
    print(max_value)
    print(min_value)


def main():
    # 수열의 길이 입력 (숫자의 개수)
    n = int(input())

    # 수열 입력
    sequence = list(map(int, input().split()))

    # 연산자 개수 입력: +, -, *, // 순서
    sign = list(map(int, input().split()))

    # 연산자 기호를 리스트로 변환
    # 예: [2, 1, 0, 1] → ['+', '+', '-', '/']
    sign_word = []
    for i, count in enumerate(sign):
        sign_word.extend(['+', '-', '*', '/'][i] * count)

    # 계산 함수 호출
    solution(n, sequence, sign_word)


# 프로그램 시작점
if __name__ == "__main__":
    main()