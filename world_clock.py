import pytz
from datetime import datetime

itz = pytz.timezone('Asia/Kolkata')
etz = pytz.timezone('America/New_York')
ltz = pytz.timezone('Europe/London')

print("Time in india = ", datetime.now(tz=itz))
print("Time in New york = ", datetime.now(tz=etz))
print("Time in London = ", datetime.now(tz=ltz))