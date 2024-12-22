def solution():
    t = int(input())

    # 결과
    result = []

    for _ in range(t):
        words = ''
        r, s = map(str, input().split())

        for word in s:
            for _ in range(int(r)):
                words += word
        
        result.append(words)
    
    for i in result:
        print(i)

solution()