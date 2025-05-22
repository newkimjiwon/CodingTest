answer = 0


def calculate_expression(arr):
    total = 0
    for i in range(len(arr) - 1):
        total += abs(arr[i] - arr[i + 1])
    return total


def solution(arr, n):
    visited = [False] * n

    def dfs(path):
        global answer
        if len(path) == n:
            answer = max(answer, calculate_expression(path))
            return

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(path + [arr[i]])
                visited[i] = False

    dfs([])


def main():
    global answer

    n = int(input())
    arr = list(map(int, input().split()))

    solution(arr, n)

    print(answer)


if __name__=="__main__":
    main()