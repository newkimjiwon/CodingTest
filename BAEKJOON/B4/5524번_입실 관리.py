if __name__=="__main__":
    # 결과 값을 담는 배열
    answer = []

    # n의 개수
    n = int(input())

    for _ in range(n):
        rooms = input()
        rooms = rooms.lower()
        answer.append(rooms)

    for i in answer:
        print(i)