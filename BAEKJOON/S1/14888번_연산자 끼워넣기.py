INF = 1000000001


def dfs(numbers, sign_word, n, count, current_result, used, answer):
    if count == n - 1:  # 모든 연산자를 사용했으면 최댓값, 최솟값 갱신
        answer[0] = max(current_result, answer[0])
        answer[1] = min(current_result, answer[1])
        return

    for i in range(n - 1):
        if not used[i]:  # 아직 사용하지 않은 연산자라면
            used[i] = True
            new_result = current_result

            if sign_word[i] == '+':
                new_result += numbers[count + 1]
            elif sign_word[i] == '-':
                new_result -= numbers[count + 1]
            elif sign_word[i] == '*':
                new_result *= numbers[count + 1]
            elif sign_word[i] == '/':
                if numbers[count + 1] == 0:  # 0으로 나누기 방지
                    used[i] = False
                    continue
                # 음수 나눗셈 처리
                if new_result < 0:
                    new_result = -(-new_result // numbers[count + 1])
                else:
                    new_result //= numbers[count + 1]

            dfs(numbers, sign_word, n, count + 1, new_result, used, answer)
            used[i] = False  # 백트래킹


def main():
    n = int(input())  # n개로 이루어진 수열
    numbers = list(map(int, input().split()))
    sign = list(map(int, input().split()))

    # 연산자 리스트 생성
    sign_word = []
    for i, count in enumerate(sign):
        sign_word.extend(['+', '-', '*', '/'][i] * count)

    # 최댓값, 최솟값 초기화
    answer = [-INF, INF]
    used = [False] * (n - 1)

    # DFS 수행
    dfs(numbers, sign_word, n, 0, numbers[0], used, answer)

    # 결과 출력
    print(answer[0])  # 최댓값
    print(answer[1])  # 최솟값

main()