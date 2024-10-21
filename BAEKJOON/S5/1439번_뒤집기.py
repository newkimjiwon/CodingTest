# 문자열 입력
s = list(input())

# 0과 1의 개수를 셈
count_one = 0
count_zero = 0

# 첫 번째 문자에 따라 처음 시작할 때 한 번 카운팅
if s[0] == '0':
    count_zero += 1
else:
    count_one += 1

# 1번째 문자부터 끝까지 연속된 구간이 바뀔 때 카운팅
for idx in range(1, len(s)):
    if s[idx] != s[idx - 1]:  # 연속된 숫자가 바뀌는 지점에서 카운트 증가
        if s[idx] == '1':
            count_one += 1
        else:
            count_zero += 1

# 최소 뒤집기 횟수는 두 그룹 중 더 적은 그룹을 뒤집는 것
print(min(count_one, count_zero))