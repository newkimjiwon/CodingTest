import sys
input = sys.stdin.read

# 입력을 한 번에 읽어오기
data = input().split()

n = int(data[0])  # 포켓몬 개수
m = int(data[1])  # 문제 개수

# 포켓몬 저장 (1번째 포켓몬부터)
pokemon = [""] + data[2:n+2]  # 포켓몬 리스트 (1-based index)

# 포켓몬 이름 -> 번호 매핑을 위한 딕셔너리
pokemon_dict = {name: i for i, name in enumerate(pokemon) if i != 0}

# m개의 문제 처리
target = data[n+2:]

# 결과 출력
for t in target:
    if t.isdigit():  # 숫자면 포켓몬 이름 출력
        print(pokemon[int(t)])
    else:  # 이름이면 포켓몬 번호 출력
        print(pokemon_dict[t])