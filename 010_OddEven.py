number = int(input("Which number do you want to check? "))

r = number % 2
if r == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")
