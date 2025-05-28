def solution(channel, usable_buttons):
    min_clicks = abs(channel - 100)  # 초기값: +,- 버튼만 사용

    for num in range(1000000):  # 0부터 999999까지 전체 탐색
        str_num = str(num)
        for ch in str_num:
            if int(ch) not in usable_buttons:
                break
        else:
            # 이 숫자는 리모컨으로 누를 수 있음
            press_count = len(str_num) + abs(channel - num)
            min_clicks = min(min_clicks, press_count)

    return min_clicks


def main():
    channel = int(input())
    breakdown = int(input())

    # usable_button = 누를 수 있는 번호
    # broken_buttons = 부서진 번호
    if breakdown:
        broken_buttons = list(map(int, input().split()))
        usable_buttons = [i for i in range(10) if i not in broken_buttons]
    else:
        usable_buttons = list(range(10))

    print(solution(channel, usable_buttons))


if __name__=="__main__":
    main()