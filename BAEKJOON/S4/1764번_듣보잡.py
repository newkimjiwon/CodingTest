n, m = map(int, input().split())

people = {}

result = []

for _ in range(n):
    person = input()
    # 듣도 못한 사람의 이름을 입력 받아서 딕셔너리로 저장
    if not people.get(person):
        people[person] = 1

for _ in range(m):
    find = input()
    # 듣도 못한 사람의 이름을 입력 받아서 딕셔너리에 있으면 이름을 출력
    if people.get(find):
        result.append(find)

# 사전순으로 정렬
result.sort()

# 듣보잡으 수를 출력
print(len(result))

for i in result:
    print(i)