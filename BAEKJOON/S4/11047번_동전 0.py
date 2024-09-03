N, K = map(int, input().split())

# 코인 지갑
coins = [int(input()) for _ in range(N)]

# 코인 개수
cnt = 0
# 나머지
money = 0

coins.sort(reverse = True)

for coin in coins:
    if K == 0:
        break
    if K < coin:
        continue
    else:
        cnt += K // coin
        K %= coin

print(cnt)