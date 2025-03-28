def solve(n, y, col, diag1, diag2, result):
    if y == n:
        result[0] += 1
        return

    for x in range(n):
        if not col[x] and not diag1[y + x] and not diag2[y - x + n - 1]:
            col[x] = diag1[y + x] = diag2[y - x + n - 1] = True
            solve(n, y + 1, col, diag1, diag2, result)
            col[x] = diag1[y + x] = diag2[y - x + n - 1] = False


def main():
    n = int(input())
    col = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    result = [0]
    solve(n, 0, col, diag1, diag2, result)
    print(result[0])


if __name__ == "__main__":
    main()