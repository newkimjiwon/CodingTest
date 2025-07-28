import sys 


def solution(n, d, k, c, sushi):
    eaten = [0] * (d + 1)
    eaten[c] = 1
    count = 1

    for i in range(k):
        if eaten[sushi[i]] == 0:
            count += 1
        eaten[sushi[i]] += 1
    
    max_count = count

    for i in range(1, n):
        eaten[sushi[i-1]] -= 1
        if eaten[sushi[i-1]] == 0:
            count -= 1

        right_idx = (i + k - 1) % n
        if eaten[sushi[right_idx]] == 0:
            count += 1
        eaten[sushi[right_idx]] += 1

        max_count = max(max_count, count)

    return max_count


def main():
    n, d, k, c = map(int, sys.stdin.readline().split())

    sushi = []

    for _ in range(n):
        s = int(sys.stdin.readline()) 
        sushi.append(s)

    print(solution(n, d, k, c, sushi))


if __name__=="__main__":
    main()