import math


def count_positions(x1, y1, r1, x2, y2, r2):
    dist = math.hypot(x2 - x1, y2 - y1)  # 두 중심 사이 거리

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            return -1  # 같은 원
        else:
            return 0   # 중심 같지만 반지름 다름

    if dist > r1 + r2:
        return 0  # 두 원이 떨어져 있음
    elif dist < abs(r1 - r2):
        return 0  # 한 원이 다른 원 내부에 있음
    elif dist == abs(r1 - r2) or dist == r1 + r2:
        return 1  # 내접 or 외접
    else:
        return 2  # 두 점에서 만남


def main():
    T = int(input())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        print(count_positions(x1, y1, r1, x2, y2, r2))


if __name__=='__main__':
    main()
