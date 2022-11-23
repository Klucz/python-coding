import calendar

cal = calendar.TextCalendar(firstweekday=3)  # Create an instance firstweekday: 0=monday, etc
cal.pryear(2022)  # What happens here?
print('\n\n\n')
cal.prmonth(2022, 3)  # print March 2022

d = calendar.LocaleTextCalendar(6, "SPANISH")
d.pryear(2012)

print(calendar.isleap(2022))  # check if specified year is a leap year
