
def main():
    n = int(input())  # n는 팔린 책의 수

    books = {}  # 팔린 책 표시

    answer = []  # 결과 값을 담는 배열

    for _ in range(n):
        book = input()  # 책
        if not books.get(book):  # 처음 나오는 책인 경우 1를 넣고 아닌 팔린 적이 있는 경우 += 1 해준다.
            books[book] = 1
        else:
            books[book] += 1

    max_sell = max(books.values())  # 가장 많이 팔린 권

    for b in books:  # 모든 책을 볼 예정
        if books[b] == max_sell:
            answer.append(b)  # 동일한 권이 있을 경우가 있을 경우

    answer.sort()  # 사전 순으로 정렬 == 오름차순으로 정렬

    print(answer[0])  # 가장 첫 번째에 있는 책 표시

if __name__=="__main__":
    main()