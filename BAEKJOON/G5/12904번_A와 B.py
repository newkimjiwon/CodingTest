def solution(s, t):
    t = list(t)  # 문자열을 리스트로 변환하여 수정 가능하게 만듦

    while len(t) > len(s):
        if t[-1] == 'A':
            t.pop()  # 마지막 문자 제거
        else:
            t.pop()  # 마지막 문자 제거
            t.reverse()  # 문자열 뒤집기

    return 1 if ''.join(t) == s else 0


def main():
    s = input().strip()  # 공백 제거
    t = input().strip()

    print(solution(s, t))


if __name__ == "__main__":
    main()