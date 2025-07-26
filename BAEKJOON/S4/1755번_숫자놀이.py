# 1. M과 N을 입력받습니다.
m, n = map(int, input().split())

# 2. 숫자(인덱스)에 해당하는 영어 단어를 리스트에 저장합니다.
digit_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# 3. M부터 N까지의 숫자를 리스트로 만듭니다.
numbers = list(range(m, n + 1))

# 4. 숫자를 영어 단어 문자열로 변환하는 함수를 정의합니다.
def num_to_words(num):
    # 숫자를 문자열로 바꾸고(e.g., 81 -> "81"), 각 자릿수를 영어로 변환하여 리스트에 담습니다.
    # "81" -> ["eight", "one"]
    words = [digit_words[int(digit)] for digit in str(num)]
    return ' '.join(words)

# 5. key 함수를 사용하여 numbers 리스트를 정렬합니다.
sorted_numbers = sorted(numbers, key=lambda num: ' '.join(digit_words[int(d)] for d in str(num)))

# 6. 정렬된 결과를 10개씩 끊어서 출력합니다.
for i in range(len(sorted_numbers)):
    print(sorted_numbers[i], end=' ')
    if (i + 1) % 10 == 0:
        print()