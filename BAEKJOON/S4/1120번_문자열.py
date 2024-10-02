def min_difference(A, B):
    len_a = len(A)
    len_b = len(B)

    min_diff = float('inf')

    # B에서 A를 삽입할 수 있는 모든 위치에 대해 계산
    for i in range(len_b - len_a + 1):
        count = 0
        for j in range(len_a):
            if A[j] != B[i + j]:
                count += 1
        min_diff = min(min_diff, count)

    return min_diff


A, B = input().split()
print(min_difference(A, B))