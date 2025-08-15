total = 10000
effort = 5

days = total // effort
hours = total % effort

months = days // 30
days = days % 30

years = months // 12
months = months % 12

print(years, "yrs", months, "months", days, "days", hours, "hrs")
