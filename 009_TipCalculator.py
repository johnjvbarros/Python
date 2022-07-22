print("welcome to the print calculator")
total = float(input("What was the total bill? $"))
tip = float(input("What % tip would you like to give? 10 12 or 15? "))
people = int(input("How many people to split the bill? "))

total_usd = total * (1 + tip/100)
total_per_person = round(total_usd / people, 2)
final_amount = "{:.2f}".format(total_per_person)
print(f"Each person should pay: ${final_amount}")
