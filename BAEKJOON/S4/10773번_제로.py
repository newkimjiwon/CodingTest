def solution():
    # 정수 k를 입력
    k = int(input())

    # 스택
    stack = []

    for _ in range(k):
        money = int(input())
        if money == 0:
            if stack:
                stack.pop()
        else:
            stack.append(money)
    
    print(sum(stack))
    

if __name__=="__main__":
    solution()