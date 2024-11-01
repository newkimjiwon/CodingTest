T = int(input())
for _ in range(T):
    N = int(input())
    a, b = 1, 0 # 0과 1이 호출된 횟수
    for i in range(N):
        # 0은 1이 호출된 횟수만큼, 1은 0과 1이 호출된 합만큼 출력됨
        a, b = b, a + b
    print(a, b)