def solution(N):
    count = 0
    target = 1

    # 팩토리얼 계산
    for i in range(1, N + 1):
        target = target * i

    while target % 10 == 0:
        target //= 10
        count += 1

    return count

n = int(input())

print(solution(n))

"""
이 방법은 주어진 N까지 5, 25, 125 등 5의 거듭제곱들이 몇 번 등장하는지를 계산하여 count에 더해주는 방식입니다.
예를 들어, N이 100일 경우 5의 배수는 20개, 25의 배수는 4개, 125의 배수는 없기 때문에, 최종적으로 count에는 20 + 4 = 24가 저장되어 0의 개수가 24개가 됩니다.

이 방법의 시간 복잡도는 O(log_5(N))으로, 초기의 O(N)보다 훨씬 효율적입니다. N이 커질수록 성능 차이가 크게 발생합니다.

def solution(N):
    count = 0
    i = 5
    while N >= i:
        count += N // i
        i *= 5
    return count

n = int(input())

print(solution(n))
"""