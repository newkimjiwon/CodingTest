if __name__=="__main__":
    N = int(input())

    for i in range(N):
        star = '*'
        space = ''

        for j in range(i):
            star += '*'
        
        for k in range(i, N - 1):
            space += ' '
        
        print(star + space + space + star)
    
    for i in range(N):
        star = ''
        space = ' '

        for j in range(i, N - 1):
            star += '*'
        
        for k in range(i):
            space += ' '
        
        print(star + space + space + star)