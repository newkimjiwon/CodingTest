if __name__=="__main__":
    a, b = map(int, input().split())
    c = int(input())

    total = (a * 60) + b + c

    hour = (total // 60) % 24
    minute = total % 60

    print(hour, minute)