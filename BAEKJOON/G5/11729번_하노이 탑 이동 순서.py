def hanoi(n, start, end, aux):
    """
    n개의 원판을 start 장대에서 end 장대로 aux 장대를 거쳐 옮깁니다.
    """
    # 1. 기본 단계 (Base Case): 원판이 1개일 때
    if n == 1:
        print(start, end)
        return

    # 2. 재귀 단계 (Recursive Step)
    # 2-1. n-1개의 원판을 start에서 aux로 옮긴다 (end를 보조로)
    hanoi(n - 1, start, aux, end)
    
    # 2-2. n번째 (가장 큰) 원판을 start에서 end로 옮긴다
    print(start, end)
    
    # 2-3. n-1개의 원판을 aux에서 end로 옮긴다 (start를 보조로)
    hanoi(n - 1, aux, end, start)

# 1. 입력 받기
N = int(input())

# 2. 총 이동 횟수 K 출력
print(2**N - 1)

# 3. 이동 순서 출력 (1번 장대 -> 3번 장대, 2번 장대 보조)
hanoi(N, 1, 3, 2)