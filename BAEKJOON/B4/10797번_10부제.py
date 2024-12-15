def main():
    n = int(input())
    cars = list(map(int, input().split()))

    answer = 0

    for car in cars:
        if n == car:
            answer += 1
    
    print(answer)

main()