def testset(arr):
    if sum(arr) == 0:
        return '0'
    elif sum(arr) > 0:
        return '+'
    elif sum(arr) < 0:
        return '-'

for _ in range(3):
    n = int(input())
    result = [int(input()) for _ in range(n)]
    print(testset(result))