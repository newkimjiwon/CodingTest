def solution():
    answer = 0

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(n):
        total = arr[i]

        if total == m:
            answer += 1
            continue
        for ii in range(i + 1, n):
            total += arr[ii]

            if total == m:
                answer += 1
                break
            elif total > m:
                break
    
    print(answer)


if __name__=="__main__":
    solution()