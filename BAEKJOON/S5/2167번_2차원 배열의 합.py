import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0

    n = int(data[idx])   # 행
    idx += 1
    m = int(data[idx])   # 열
    idx += 1

    chart = [[0] * (m + 1) for _ in range(n + 1)]
    prefix = [[0] * (m + 1) for _ in range(n + 1)]

    # 입력 및 누적합 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            chart[i][j] = int(data[idx])
            idx += 1
            prefix[i][j] = (
                prefix[i-1][j]
                + prefix[i][j-1]
                - prefix[i-1][j-1]
                + chart[i][j]
            )

    k = int(data[idx])
    idx += 1
    output = []

    for _ in range(k):
        i = int(data[idx])
        idx += 1
        j = int(data[idx])
        idx += 1
        x = int(data[idx])
        idx += 1
        y = int(data[idx])
        idx += 1

        result = (
            prefix[x][y]
            - prefix[i-1][y]
            - prefix[x][j-1]
            + prefix[i-1][j-1]
        )
        output.append(str(result))

    print("\n".join(output))

main()