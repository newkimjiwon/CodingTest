if __name__=="__main__":
    T = int(input())

    for _ in range(T):
        words = input()
        if len(words) >= 6 and len(words) <= 9:
            print('yes')
        else:
            print('no')