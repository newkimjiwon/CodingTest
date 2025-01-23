def binary_search(tree, m):
    # 결과 값
    answer = 0
    # 이진 탐색을 위한 변수
    left = 0
    right = max(tree)

    # 경우의 수
    while left <= right:
        # 나무를 자른 결과 값
        total = 0

        # 자르는 높이의 길이의 중간 지점
        slice_high = (left + right) // 2

        # 나무 잘라서 total에 대입
        for t in tree:
            if t > slice_high:
                total += t - slice_high

        # 자른 나무의 길이가 길면 높여야 한다.
        if total < m:
            right = slice_high - 1
        # 나무의 양이 충분하다면 result에 저장 밑 오른쪽 부분 탐색
        else:
            answer = slice_high
            left = slice_high + 1

    return answer


def main():
    # 나무의 수 N과 나무의 길이 M이 주어진다.
    n, m = map(int, input().split())
    # 나무
    tree = list(map(int, input().split()))

    print(binary_search(tree, m))


main()