while True:
    answer = int(input("Enter in a number within 1 to 100"))
    if -1<answer<101:
        break

if -1<answer<36:
    print("Your grade is U.")
elif 34<answer<45:
    print("Your grade S.")
elif 44<answer<50:
    print("Your grade is E.")
elif 49<answer<55:
    print("Your grade is D.")
elif 54<answer<60:
    print("Your grade is C.")
elif 59<answer<70:
    print("Your grade is B.")
elif 69<answer<101:
    print("Your grade is A.")
