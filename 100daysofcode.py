from datetime import date

start = date(2020, 1, 1)
today = date.today()
delta = today - start

if (delta.days < 101):
    print("Today is day {}".format(delta.day))
else:
    print('100 Days of Code sprint has ended')
