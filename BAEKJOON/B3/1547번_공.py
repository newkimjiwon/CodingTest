def main():
    # 컵 변경 횟수
    m = int(input())
    # 정답 컵 (1 ~ 3)
    answer = 1

    for _ in range(m):
        f, s = map(int, input().split())
        if f == answer or s == answer:
            if f != answer:
                answer = f
            elif s != answer:
                answer = s
    
    print(answer)
    
main()