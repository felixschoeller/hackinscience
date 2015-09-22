import time
import daytime
today = datetime.date.today()
localtime = time.localtime(time.time())

print("Today is", today, "and the time is", localtime)