def count_non_overlapping_occurrences(document, word):
    count = 0
    index = 0

    while True:
        index = document.find(word, index)
        if index == -1:
            break
        count += 1
        index += len(word)  # 겹치지 않게 이동

    return count


def main():
    # 입력
    document = input().strip()
    word = input().strip()

    # 출력
    print(count_non_overlapping_occurrences(document, word))


main()