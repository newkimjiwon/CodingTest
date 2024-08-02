def VPS(st):
    stack = []

    for i in st:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return "NO"
            
    if not stack:
        return "YES"
    else:
        return "NO"
    
N = int(input())

for _ in range(N):
    PS = input()
    print(VPS(PS))