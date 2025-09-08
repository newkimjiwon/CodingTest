if __name__=="__main__":
    n = int(input())

    for i in range(n):
        star = '*'
        space = ''

        for _ in range(i):
            space += ' '

        for _ in range(2 * (n - i - 1)):
            star += '*'
        
        print(space + star)

    for i in range(n - 1):
        star = '*'
        space = ''

        for _ in range(i, n - 2):
            space += ' '

        for _ in range(2 * (i + 1)):
            star += '*'
        
        print(space + star)