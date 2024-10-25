# 입력받기
N = int(input().strip())
F = int(input().strip())

# N의 마지막 두 자리를 00부터 99로 변경하면서 검사
for i in range(100):
    # 새로운 N 생성 (마지막 두 자리를 i로 변경)
    new_N = (N // 100) * 100 + i
    if new_N % F == 0:
        # 두 자리 수가 10보다 작으면 0을 붙여서 출력
        print(f"{i:02d}")
        break