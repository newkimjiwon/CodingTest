n = int(input())  # 학생 수 입력
students = [list(map(int, input().split())) for _ in range(n)]  # 학생들의 반 정보 입력

# 같은 반 학생 수를 저장할 리스트
same_class_counts = [0] * n

# 각 학생에 대해 비교
for i in range(n):
    for j in range(n):
        if i != j:  # 자신과는 비교하지 않음
            for grade in range(5):  # 1학년부터 5학년까지
                if students[i][grade] == students[j][grade]:
                    same_class_counts[i] += 1
                    break  # 같은 반을 확인했으면 더 이상 비교하지 않음

# 가장 많은 같은 반 학생 수를 가진 학생 찾기
max_count = max(same_class_counts)
result = same_class_counts.index(max_count) + 1  # 학생 번호는 1부터 시작하므로 +1

print(result)