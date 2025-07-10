import time


# 윤년 판별 함수
def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


# 각 월의 일수 (평년 기준)
# 인덱스 0은 비워두고, 1월부터 12월까지 순서대로 일수를 저장
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution():
    months, day, year, times= map(str, input().split())
    year = int(year)
    day = int(day[:-1])  # 날짜 , 자르기

    hour, minute = map(int, times.split(':'))  # 시간, 분 자르기

    # 12개월
    years = {'January': 1, 'February': 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
             "August": 8, 'September': 9, "October": 10, "November": 11, "December": 12}
    
    month = years[months] # 월 이름 숫자로 변환

    # 1. 해당 연도의 총 분 계산
    total_days_in_year = 365
    if is_leap_year(year):
        total_days_in_year = 366
    
    total_minutes_in_year = total_days_in_year * 24 * 60

    # 2. 현재까지 지난 분 계산
    minutes_passed_this_year = 0

    # 지난 달들의 일수 합산
    for m in range(1, month): # 1월부터 현재 월 직전까지
        minutes_passed_this_year += days_in_month[m] * 24 * 60
        # 윤년이고 2월을 지난 경우 2월에 하루 추가 (3월 1일 이후부터 적용)
        if is_leap_year(year) and m == 2:
            minutes_passed_this_year += 1 * 24 * 60 # 2월이 29일이므로 하루치 분 추가

    # 현재 달의 지난 일수 합산
    minutes_passed_this_year += (day - 1) * 24 * 60 # 현재 일은 그 전날까지는 완전히 지났으므로 (day-1)

    # 현재 일의 지난 시간과 분 합산
    minutes_passed_this_year += hour * 60
    minutes_passed_this_year += minute

    # 3. 퍼센트 계산
    # 소수점 정확도를 위해 float으로 계산
    percentage = (minutes_passed_this_year / total_minutes_in_year) * 100
    
    # 결과 출력
    print(percentage)


if __name__=="__main__":
    solution()