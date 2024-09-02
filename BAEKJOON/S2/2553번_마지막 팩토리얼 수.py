def solution(n):
    dp = 1

    for i in range(2, n + 1):
        dp *= i

    return dp

N = int(input())
st = str(solution(N))
stt = st[::-1]

for i in range(len(stt)):
    if int(stt[i]) != 0:
        print(int(stt[i]))
        break