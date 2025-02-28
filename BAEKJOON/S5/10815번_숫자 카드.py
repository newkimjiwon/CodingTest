if __name__=="__main__":
    answer = {}  # 정답 딕셔너리
    
    n = int(input())  # 상근 카드 수
    sang = list(map(int, input().split()))  # 상근의 카드

    m = int(input())  # 카드 수
    check = list(map(int, input().split()))

    for i in check:
        answer[i] = 0
    
    for j in sang:
        if not answer.get(j):
            answer[j] = 1
    
    for k in check:
        print(answer[k], end = ' ')