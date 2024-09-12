S = input()

def min_a(word):
    # 처음 a의 개수
    total_a = word.count('a')

    # 원형이라고 했으니깐 두 문자열을 붙여준다.
    ac = word + word

    # 원형 문자열에서 a의 개수를 검사
    current_a = ac[:total_a].count('a')
    max_a = current_a # a가 가장 많을 때랑 비교할 변수다

    for i in range(1, len(word)):
        if ac[i - 1] == 'a':
            current_a -= 1
        if ac[total_a + i - 1] == 'a':
            current_a += 1
        max_a = max(max_a, current_a)
    # a가 최대가 되면 최소화된 b의 개수만 남는다
    return total_a - max_a

print(min_a(S))