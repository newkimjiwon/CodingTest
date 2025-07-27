def main():
    n = int(input())

    result = []

    for _ in range(n):
        number = int(input())
        result.append(number)

    result.sort()

    for i in result:
        print(i)


main()