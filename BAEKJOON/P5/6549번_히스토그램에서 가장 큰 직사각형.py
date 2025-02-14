def solution(histogram):
    stack = []  # 인덱스를 저장하는 스택
    max_area = 0  # 최대 직사각형 넓이
    histogram.append(0)  # 마지막에 0을 추가하여 남은 요소를 처리하기 쉽게 함

    for i in range(len(histogram)):
        # 스택이 비어있지 않고 현재 막대가 스택 top의 막대 높이보다 낮다면 pop 진행
        while stack and histogram[stack[-1]] > histogram[i]:
            height = histogram[stack.pop()]  # pop된 높이
            width = i if not stack else (i - stack[-1] - 1)  # 너비 계산
            max_area = max(max_area, height * width)  # 최대 넓이 갱신

        stack.append(i)  # 현재 인덱스를 스택에 push

    return max_area


def main():
    # 결과
    result = []

    while True:
        # 테스트 케이스
        t = list(map(int, input().split()))

        if t[0] == 0:
            break
        else:
            result.append(solution(t[1:]))

    for i in result:
        print(i)


if __name__=="__main__":
    main()