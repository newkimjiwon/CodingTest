def solution(numbers):
    # 정렬
    numbers.sort()
    
    # 필요한 최소 추가 숫자 계산
    min_additions = float('inf')
    
    for i in range(len(numbers)):
        # 현재 숫자를 기준으로 5개의 숫자를 포함하는 구간 설정
        start = numbers[i]
        end = start + 4  # 5개의 연속된 숫자 구간
        
        # 구간 내 숫자들을 계산
        count_in_range = sum(start <= num <= end for num in numbers)
        additions = 5 - count_in_range
        
        # 최소 추가 숫자 갱신
        min_additions = min(min_additions, additions)
    
    return min_additions

if __name__ == "__main__":
    # 정수의 개수
    n = int(input())

    # 정수 배열
    numbers = [int(input()) for _ in range(n)]

    print(solution(numbers))
