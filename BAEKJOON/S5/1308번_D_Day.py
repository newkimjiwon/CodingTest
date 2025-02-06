from datetime import date


def main():
    # 입력 받기
    y1, m1, d1 = map(int, input().split())
    y2, m2, d2 = map(int, input().split())

    # 천년 이상 차이가 나면 "gg" 출력
    if y2 - y1 > 1000 or (y2 - y1 == 1000 and (m2, d2) >= (m1, d1)):
        print("gg")
    else:
        # 날짜 차이 계산
        d1 = date(y1, m1, d1)
        d2 = date(y2, m2, d2)
        diff = (d2 - d1).days
        print(f"D-{diff}")


if __name__ == "__main__":
    main()
