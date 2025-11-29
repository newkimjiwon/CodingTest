def solution():
    K, N, M = map(int, input().split())

    return (K * N) - M if (K * N) - M > 0 else 0

if __name__=="__main__":
    print(solution())