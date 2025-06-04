import heapq
import sys


def solution():
    input = sys.stdin.readline
    write = sys.stdout.write
    
    heap = []
    answer = []
    n = int(input())

    for _ in range(n):
        num = int(input())
        if num != 0:
            heapq.heappush(heap, -num)
        else:
            if not heap:
                answer.append('0\n')
            else:
                answer.append(f"{-heapq.heappop(heap)}\n")

    write(''.join(answer))


if __name__ == "__main__":
    solution()