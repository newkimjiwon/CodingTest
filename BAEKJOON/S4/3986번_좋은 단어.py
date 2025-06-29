def solution(n, words):
    stack = []

    for i in words:
        if stack and stack[-1] == i:
            stack.pop()
            continue
        
        stack.append(i)

    # stack에 남아있으면 False 없으면 True
    if stack:
        return False
    else:
        return True
        
        
def main():
    n = int(input())

    answer = 0

    for _ in range(n):
        word = list(input())

        if solution(n, word):
            answer += 1
    
    print(answer)


main()