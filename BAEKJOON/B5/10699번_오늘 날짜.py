from datetime import datetime, timedelta, timezone

kst = timezone(timedelta(hours=9))
print(datetime.now(kst).strftime("%Y-%m-%d"))