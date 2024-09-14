def matrix_mult(A, B, m):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % m, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % m],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % m, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % m]]

def matrix_pow(M, power, m):
    result = [[1, 0], [0, 1]]  # 단위 행렬
    base = M

    while power > 0:
        if power % 2 == 1:
            result = matrix_mult(result, base, m)
        base = matrix_mult(base, base, m)
        power //= 2

    return result

def fibonacci_mod(n, m):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # 피보나치 수를 위한 기본 행렬 [[1, 1], [1, 0]]
    F = [[1, 1], [1, 0]]

    # F^n-1을 계산
    result = matrix_pow(F, n - 1, m)

    # 최종 결과는 행렬의 [0][0] 값
    return result[0][0]

n = int(input())
m = 1000000007
print(fibonacci_mod(n, m))