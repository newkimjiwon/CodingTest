import itertools

a, b = map(str, input().split())

a_l, b_l = list(a), list(b)

result_a = 0
result_b = 0

# zip_longest를 사용하여 짧은 리스트의 끝을 채워줌 (디폴트값 0)
for i, j in itertools.zip_longest(a_l, b_l, fillvalue='0'):
    result_a += int(i)
    result_b += int(j)

print(result_a * result_b)