def main():
    result = list(map(int, input().split()))
    answer = 0

    for i in result:
        answer += i * i

    print(answer % 10)

main()