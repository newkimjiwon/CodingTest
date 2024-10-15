n, l = map(int, input().split())

label = ['0'] * (n + 1)
label_idx = 0
idx = 0
number_first = []
number_rest = []

# 첫 자리에는 0을 제외한 숫자만 가능
for i in range(1, 10):
    if i != l:
        number_first.append(str(i))

# 나머지 자리에는 0 ~ 9 중 l을 제외한 숫자를 사용
for i in range(10):
    if i != l:
        number_rest.append(str(i))

# 1자리 수부터 시작
for i in number_first:
    label[idx] = i
    idx += 1
    if idx == n:
        break

# 2자리 이상의 수 생성
if idx < n:
    while idx < n:
        for i in number_rest:
            label[idx] = label[label_idx] + i
            idx += 1
            if idx == n:
                break
        label_idx += 1

# 마지막으로 붙인 라벨 출력
print(int(label[n - 1]))