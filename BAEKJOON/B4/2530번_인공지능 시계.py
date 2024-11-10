h, m, s = map(int, input().split())
user_input = int(input())

user_hour = user_input // 3600
user_input %= 3600
user_minute = user_input // 60
user_input %= 60
user_second = user_input

if s + user_second >= 60:
    s = (s + user_second) % 60
    user_minute += 1
else:
    s = s + user_second

if m + user_minute >= 60:
    m = (m + user_minute) % 60
    user_hour += 1
else:
    m = m + user_minute

if h + user_hour >= 24:
    h = (h + user_hour) % 24
else:
    h = (h + user_hour)

print(h, m, s)