N = int(input())
A = list(map(int, input().split()))

A.sort()

# 개수를 셀 변수
cnt = 0

for k in range(N):
    left = 0
    right = N - 1
    
    while left < right:
        if left == k:  # left가 기준 인덱스를 가리키면 건너뜀
            left += 1
            continue
        if right == k:  # right가 기준 인덱스를 가리키면 건너뜀
            right -= 1
            continue
            
        current_sum = A[left] + A[right]
        
        if current_sum == A[k]:
            cnt += 1
            break
        elif current_sum < A[k]:
            left += 1
        else:
            right -= 1

print(cnt)