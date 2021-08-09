import datetime

now = datetime.now()
start = now.replace(hour = int('%H'), minute = int('%M'))
# end = now.replace(hour = int(end_hour), minute = int(end_minute))

print(start)