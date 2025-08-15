total = 10000
#effort = 5
effort = int(input("what is your  daily efforts? "))

days = total // effort
hours = total % effort

months = days // 30
rem_days = days % 30

years = months // 12
rem_months = months % 12

print(years, "yrs", rem_months, "months", rem_days, "days", hours, "hrs")
