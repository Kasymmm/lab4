#Write a Python program to subtract five days from current date.

from datetime import date, timedelta
today=date.today()
old=today-timedelta(5)
print(today.strftime("%D"))
print(old.strftime("%D"))