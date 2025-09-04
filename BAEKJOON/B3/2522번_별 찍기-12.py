if __name__=="__main__":
    n = int(input())

    for i in range(n):
        star = '*'
        space = ''

        for ii in range(i, n - 1):
            space += ' '
        for iii in range(i):
            star += '*'
        
        print(space + star)

    for i in range(n - 1):
        star = ''
        space = ' '

        for ii in range(i):
            space += ' '
        for iii in range(i, n - 1):
            star += '*'
        
        print(space + star)