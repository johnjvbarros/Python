# Python If-Else Challenge
n = int(input("Type a number between 0 and 100:\n"))
while n < 101:
    if n % 2 == 1:
        print("Weird")
    elif n > 20:
        print("Not Weird")
    elif n > 6:
        print("Weird")
    else:
        print("Not Weird")
    break
