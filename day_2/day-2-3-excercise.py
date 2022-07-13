# ?? Don't change the code below ??
age = input("What is your current age?")
# ?? Don't change the code above ??

#Write your code below this line ??
years_remaining = 90 - int(age)

days_int = int(years_remaining * 365)
weeks_int = int(years_remaining * 52)
months_int = int(years_remaining * 12)

print(f'You have {days_int} days, {weeks_int} weeks, and {months_int} months left.')
