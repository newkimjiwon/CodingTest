import heapq


def main():
    n = int(input())  # n번째로 큰 수
    heap = []

    for _ in range(n):
        numbers = list(map(int, input().split()))
        for num in numbers:
            heapq.heappush(heap, num)
            if len(heap) > n:
                heapq.heappop(heap)

    print(heap[0])  # 최소 힙이므로, n번째로 큰 값이 루트에 있음


if __name__ == "__main__":
    main()