n = int(input())  # 통화 개수 입력
call = list(map(int, input().split()))  # 통화 시간 리스트

# 영식 요금제 계산
y = sum((i // 30 + 1) * 10 for i in call)
# 민식 요금제 계산
m = sum((i // 60 + 1) * 15 for i in call)

# 결과 출력
if y < m:
    print("Y", y)
elif y > m:
    print('M', m)
else:
    print("Y M", y)