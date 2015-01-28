the_first_number = int(input("Enter in the first number : "))
the_second_number = int(input("Enter in the second number: "))
the_min = min(the_first_number, the_second_number)
while the_min != 0:
    if the_first_number % the_min == 0:
        if the_second_number % the_min == 0:
            print(the_min)
            break
            the_min -= 1

