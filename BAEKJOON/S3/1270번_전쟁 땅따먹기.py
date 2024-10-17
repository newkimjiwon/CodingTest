# 땅의 개수
n = int(input())

answer = []

for _ in range(n):
    win = {}
    war = list(map(int, input().split()))
    # 길이를 구할 변수
    formation = len(war)
    # 과반수를 구해야 하므로 짝수와 홀수의 경우를 나눈다.
    # ex) 7의 과반수는 4이므로 2로 나누고 1를 더해줌
    if formation % 2 == 0:
        formation //= 2
    else:
        formation //= 2
        formation += 1
    # 해쉬를 이용한 문제이므로 딕셔너리를 사용해준다.
    for i in war:
        if not win.get(i):
            win[i] = 1
        else:
            win[i] += 1
        # 중간에서 만약 과반수가 발생한다면 종료한다.
        if win.get(i) and win[i] >= formation:
            answer.append(str(i))
            break
    # 과반수가 발생하지 않았을 때
    max_value = max(win.values())
    if max_value < formation:
        answer.append("SYJKGW")

for i in answer:
    print(i)