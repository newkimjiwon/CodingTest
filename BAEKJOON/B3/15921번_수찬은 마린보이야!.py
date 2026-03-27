import sys

def solve():
    # 첫째 줄 입력: 연습 기록의 개수 N
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    
    # N이 0인 경우 예외 처리
    if n == 0:
        print("divide by zero")
        return

    # 둘째 줄 입력: 연습 기록 리스트
    records = list(map(int, input_data[1:]))
    
    # 평균 계산
    total_sum = sum(records)
    avg = total_sum / n
    
    # 기댓값 계산 (각 기록 * 1/n 의 총합)
    # 사실상 평균과 같음
    expected_value = 0
    for x in records:
        expected_value += x * (1 / n)
    
    # 분모(기댓값)가 0인 경우 예외 처리
    if expected_value == 0:
        print("divide by zero")
    else:
        # 확률 계산: 평균 / 기댓값
        probability = avg / expected_value
        # 소수점 둘째 자리까지 출력
        print(f"{probability:.2f}")

if __name__ == "__main__":
    solve()