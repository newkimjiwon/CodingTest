import sys

input = sys.stdin.read


def solution(words, k):
    # 필수적으로 배워야 하는 문자 (a, c, n, i, t)
    essential = {'a', 'c', 'n', 'i', 't'}

    # 기본적으로 5개의 단어를 요구하므로 5미만은 답이 0이다.
    if k < 5:
        return 0

    # 단어에서 필수 문자 제거 후 남은 알파벳 추출
    unique_chars = set()
    # 리스트를 이용하여 위 set() 자료형에 추가할 예정이다.
    processed_words = []

    for word in words:
        word_set = set(word) - essential  # 필수 문자 제거
        processed_words.append(word_set)
        unique_chars.update(word_set)  # 리스트에서 중복되는 원소들을 무시하고 set() 자료형으로 바뀜

    # 배울 수 있는 글자 수
    extra_k = k - 5

    # 배울 수 있는 글자가 모든 남은 글자보다 많다면 모든 단어를 읽을 수 있음
    if len(unique_chars) <= extra_k:
        return len(words)

    # 백트래킹
    unique_chars = list(unique_chars)  # set -> list
    max_read = 0  # 최대로 읽을 수 있는 단어
    selected = set(essential)  # 초기 필수 문자 포함

    def dfs(idx, count):
        nonlocal max_read  # 비전역 변수 표기
        if count == extra_k:  # 선택한 문자 개수가 K-5개가 되면 검사
            read_count = sum(1 for word in processed_words if word.issubset(selected))
            max_read = max(max_read, read_count)
            return

        for i in range(idx, len(unique_chars)):
            selected.add(unique_chars[i])
            dfs(i + 1, count + 1)
            selected.remove(unique_chars[i])  # 백트래킹 (원상 복구)

    # DFS 탐색 시작
    dfs(0, 0)

    # 정답
    return max_read


def main():
    # 단어의 개수 N과 K가 주어진다. N은 50보다 작거나 같은 자연수이고, K는 26보다 작거나 같은 자연수 또는 0이다.
    # 둘째 줄부터 N개의 줄에 남극 언어의 단어가 주어진다. 단어는 영어 소문자로만 이루어져 있고, 길이가 8보다 크거나 같고, 15보다 작거나 같다. 모든 단어는 중복되지 않는다.
    n, k = map(int, sys.stdin.readline().split())
    words = [sys.stdin.readline().strip() for _ in range(n)]
    print(solution(words, k))


if __name__ == "__main__":
    main()