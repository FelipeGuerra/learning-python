from datetime import datetime

delta = datetime.now() - datetime(1900 , 12, 31)

print(delta.days)
# print(delta.hour)
print(delta.seconds)
whenever = datetime.strptime("2017-12-31", "%Y-%m-%d")
whenever = whenever.strftime("%Y-%m")
print(whenever)