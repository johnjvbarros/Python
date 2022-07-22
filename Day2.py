number = str(input("type a 2 digit number: "))

total = int(number[0]) + int(number[1])

print(total)

# Tim Urban - Life in weeks
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
age_int = int(age)
months = (90 - age_int)*12
weeks = (90 - age_int)*52
days = (90 - age_int)*365

message = f"you have {days} days, {weeks} weeks, and {months} months left "

print(message)
