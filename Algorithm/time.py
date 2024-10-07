import time
import datetime

start = time.time()
print(9000000000000000000 // 1000000000)
end = time.time()
sec = end - start
result = datetime.timedelta(seconds = sec)
print(result)