from itertools import combinations

def is_valid(password):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    num_vowels = len([char for char in password if char in vowels])
    num_consonants = len(password) - num_vowels
    return num_vowels >= 1 and num_consonants >= 2

L, C = map(int, input().split())
words = list(map(str, input().split()))

# 정렬된 문자 리스트
words.sort()

# L 길이의 조합들을 확인
combinations_list = combinations(words, L)
valid_passwords = []

for comb in combinations_list:
    if is_valid(comb):
        valid_passwords.append(''.join(comb))

# 정렬된 암호 출력
for password in valid_passwords:
    print(password)