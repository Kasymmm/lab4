#Write a Python program to calculate two date difference in seconds

from datetime import datetime
x=datetime(2025, 2, 17, 20, 45, 00)
y=datetime(2025, 2, 13, 21, 00, 00)
difference=x-y
print(difference.total_seconds())