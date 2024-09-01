def solution(ar):
    current = [0]

    for case in ar:
        if current[-1] < case:
            current.append(case)
        else:
            left = 0
            right = len(current)

            while left < right:
                mid = (left + right) // 2
                if current[mid] < case:
                    left = mid + 1
                else:
                    right = mid
            print(current)
            current[right] = case
            print(current)
    print(current)
    return len(current) - 1

A = int(input())
cases = map(int, input().split())

print(solution(cases))