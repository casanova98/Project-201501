

answer = int(input("Enter any year to find out whether it is a leap year!"))

if answer % 4 == 0:
    if answer % 100 != 0:
        print("This is a leap year!")

if answer % 4 != 0:
    print("This is not a leap year!")

