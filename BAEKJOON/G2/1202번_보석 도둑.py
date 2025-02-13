import sys
import heapq


def solution(bags, jewel):
    # 결과 값
    answer = 0
    result = []  # 보석을 담을 최대 힙

    # 정렬 (보석: 무게 기준 오름차순, 가방: 오름차순)
    bags.sort()
    jewel.sort()

    # 가방을 하나씩 확인하며 적절한 보석을 최대 힙에 넣고 가장 비싼 걸 선택
    for bag in bags:
        while jewel and jewel[0][0] <= bag:
            heapq.heappush(result, -jewel[0][1])  # 최대 힙을 위해 음수 변환
            heapq.heappop(jewel)

        if result:
            answer -= heapq.heappop(result)  # 가장 비싼 보석 선택

    return answer


def main():
    # 빠른 입력을 위해 sys.stdin.read 사용
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    k = int(data[1])

    jewel = []
    bag = []

    index = 2
    for _ in range(n):
        m = int(data[index])
        v = int(data[index + 1])
        jewel.append([m, v])
        index += 2

    for _ in range(k):
        bag.append(int(data[index]))
        index += 1

    # 빠른 출력
    sys.stdout.write(str(solution(bag, jewel)) + "\n")


if __name__ == "__main__":
    main()