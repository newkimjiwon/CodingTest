# N, 태수의 새로운 점수 : score, P
N, score, P = map(int, input().split())

# 랭크
if N == 0:
    rank = [score]
else:
    rank = [score] + list(map(int, input().split()))
    rank.sort(reverse = True)
# 결과값
answer = 1

dic = {}

for i in rank:
    if not dic.get(i):
        dic[i] = 1
    else:
        dic[i] += 1

for r, people in dic.items():
    P -= people
    if P < 0:
        print(-1)
        break
    if r == score:
        print(answer)
        break
    else:
        answer += people