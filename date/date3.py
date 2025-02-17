#Write a Python program to drop microseconds from datetime.

from datetime import datetime
x=datetime.now()
y=x.replace(microsecond=0)
print(y)