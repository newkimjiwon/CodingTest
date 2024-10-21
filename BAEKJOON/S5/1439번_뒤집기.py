# 문자열 리스트로 변환
s = list(input())

# 0과 1의 개수를 셈
count_one = 0
count_zero = 0

s_count = 0
if s[0] == '0':
    b = 0
elif s[0] == '1':
    b = 1

s_count = False
for idx in range(1, len(s)):
    if s_count != s[idx] and s_count == 0:
        s_count = 1
        count_zero += 1
    elif s_count != s[idx] and s_count == 1:
        s_count = 0
        count_one += 1
        
if count_zero < count_one:
    print(count_zero)
else:
    print(count_one) 