from collections import defaultdict


def solve_case(word, k):
    positions = defaultdict(list)

    for idx, ch in enumerate(word):
        positions[ch].append(idx)

    min_len = float('inf')
    max_len = -1

    for ch, idx_list in positions.items():
        if len(idx_list) < k:
            continue

        for i in range(len(idx_list) - k + 1):
            start = idx_list[i]
            end = idx_list[i + k - 1]
            length = end - start + 1

            # 조건 3: 어떤 문자가 정확히 k번 포함된 가장 짧은 연속 문자열
            min_len = min(min_len, length)

            # 조건 4: 해당 문자로 시작하고 끝나는 가장 긴 연속 문자열
            if word[start] == ch and word[end] == ch:
                max_len = max(max_len, length)

    if max_len == -1:
        return "-1"
    else:
        return f"{min_len} {max_len}"


def main():
    t = int(input())

    for _ in range(t):
        word = input().strip()
        k = int(input())
        print(solve_case(word, k))


main()