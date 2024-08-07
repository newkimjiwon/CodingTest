A = int(input())
cases = map(int, input().split())
sequence = [0]

for case in cases:
    if sequence[-1] < case:
        sequence.append(case)
    else:
        left = 0
        right = len(sequence)

        while left < right:
            mid = (right+left) // 2
            if sequence[mid] < case:
                left = mid + 1
            else:
                right = mid
        sequence[right] = case

print(len(sequence)-1)