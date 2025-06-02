def solution():
    gear1 = input().strip()  # 첫 번째 기어 문자열 입력
    gear2 = input().strip()  # 두 번째 기어 문자열 입력

    len1 = len(gear1)  # 첫 번째 기어 길이
    len2 = len(gear2)  # 두 번째 기어 길이

    min_width = len1 + len2  # 최대로 겹치지 않을 경우 전체 폭 (붙여놓기)

    # gear2를 gear1에 대해 -len2 ~ +len1까지 이동 (왼쪽으로도, 오른쪽으로도)
    for shift in range(-len2, len1 + 1):
        collision = False  # 2와 2가 겹쳤는지 여부

        # gear2의 각 문자에 대해 검사
        for i in range(len2):
            g1_index = i + shift  # gear2의 i번째가 gear1의 어디와 겹치는지 계산

            # 유효한 겹침 범위일 때만 검사
            if 0 <= g1_index < len1:
                if gear1[g1_index] == '2' and gear2[i] == '2':
                    collision = True
                    break  # 맞물릴 수 없음

        if not collision:
            # 겹칠 수 있다면 전체 너비 계산
            leftmost = min(0, shift)  # 왼쪽 끝 (shift가 음수면 gear2가 더 왼쪽)
            rightmost = max(len1, shift + len2)  # 오른쪽 끝
            width = rightmost - leftmost  # 전체 너비 계산
            min_width = min(min_width, width)  # 최소 너비 갱신

    print(min_width)  # 정답 출력

if __name__ == "__main__":
    solution()