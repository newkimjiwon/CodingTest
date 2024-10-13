target = int(input())

stick = [64]

sticklen = sum(stick)

# 모든 막대의 길이 합이 목표 값과 다를 경우 계속 반복문을 돌린다.
while sticklen != target:
    # 현재 가장 작은 막대기를 뽑는다.
    # 파이썬의 리스트는 기본적으로 스택 자료구조를 가지고 있는다.
    current = stick.pop()
    # 작대기를 두 개로 나눈다.
    current_len = current // 2
    # 일단 하나는 넣어야 하므로 넣는다.
    stick.append(current_len)
    if sum(stick) < target:
        stick.append(current_len)
    sticklen = sum(stick)

print(len(stick))