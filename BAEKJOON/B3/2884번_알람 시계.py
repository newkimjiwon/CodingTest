def solution():
    hour, minute = map(int, input().split())  # 시간, 분

    minute -= 45  # 45분 일찍 맞춤

    if minute < 0:
        minute += 60 # 0보다 작아지면 내려간다.
        hour -= 1
    if hour < 0:
        hour = 23

    print(hour, minute)

if __name__=="__main__":
    solution()