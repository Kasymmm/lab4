#Write a Python program to print yesterday, today, tomorrow.

from datetime import date, timedelta
today=date.today()
yest=today-timedelta(1)
tom=today+timedelta(1)
print(yest.strftime("%D"))
print(today.strftime("%D"))
print(tom.strftime("%D"))