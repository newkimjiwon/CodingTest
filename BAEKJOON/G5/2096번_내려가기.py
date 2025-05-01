import sys
input = sys.stdin.readline


def main():
    n = int(input())

    a, b, c = map(int, input().split())
    prev_max = [a, b, c]
    prev_min = [a, b, c]

    for _ in range(1, n):
        a, b, c = map(int, input().split())

        max0 = max(prev_max[0], prev_max[1]) + a
        max1 = max(prev_max[0], prev_max[1], prev_max[2]) + b
        max2 = max(prev_max[1], prev_max[2]) + c

        min0 = min(prev_min[0], prev_min[1]) + a
        min1 = min(prev_min[0], prev_min[1], prev_min[2]) + b
        min2 = min(prev_min[1], prev_min[2]) + c

        prev_max = [max0, max1, max2]
        prev_min = [min0, min1, min2]

    print(max(prev_max), min(prev_min))


if __name__ == "__main__":
    main()