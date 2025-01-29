if __name__=="__main__":
    score = 0

    # 정답 개수
    n = int(input())
    # 정답
    ox = list(map(int, input().split()))

    # 현재 점수
    current = 0

    for i in ox:
        if i == 1:
            current += 1
            score += current
        else:
            current = 0
    
    print(score)