

answer = input("Enter your weight here. Thank you and hope you are not fat!")
answer_1 = input("Enter your height here. Thank you and hope you are not like dennis T.T")

w = float(answer)
h = float(answer_1)


BMI = w/(h*h)

if BMI <= 18.5:
    print("You are underweight!")
if 18.5<BMI<24.9:
    print("Your weight is acceptable!")
if 25<BMI<29.9:
    print("Your weight is overweight")
if BMI > 30:
    print("Your weight is getting close to obese!")




