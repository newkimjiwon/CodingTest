import sys

def check_counting():
    # 첫 번째 줄: 아이가 말한 숫자의 개수 n
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
    except ValueError:
        return

    # 아이가 말한 숫자들을 저장할 리스트
    recited_numbers = []
    for _ in range(n):
        num = int(sys.stdin.readline().strip())
        recited_numbers.append(num)

    # 아이가 마지막으로 말한 숫자
    last_number = recited_numbers[-1]
    
    # 1부터 마지막 숫자까지의 집합 생성
    full_set = set(range(1, last_number + 1))
    # 아이가 실제로 말한 숫자의 집합 생성
    recited_set = set(recited_numbers)
    
    # 빠진 숫자 찾기 (전체 집합 - 아이가 말한 집합)
    missing_numbers = sorted(list(full_set - recited_set))

    # 결과 출력
    if not missing_numbers:
        print("good job")
    else:
        for missing in missing_numbers:
            print(missing)

# 프로그램 실행
if __name__ == "__main__":
    check_counting()