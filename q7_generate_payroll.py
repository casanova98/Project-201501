#Sample input:

#Enter name: Lim Ah Seng
#Enter number of hours worked weekly: 10
#Enter hourly pay rate: 6.75
#Enter CPF contribution rate(%): 20

#Sample output:

#Payroll statement for Lim Ah Seng
#Number of hours worked in week: 10
#Hourly pay rate: $6.75
#Gross pay = $67.50
#CPF contribution at 20% = $13.50
#Net pay = $54.00

name = input("Please enter your name.")
hours = input("Please enter how many hours have you worked weekly.")
pay_rate = input("How much is your pay rate per hour?")
CPF_rate = input("Enter your CPF contribution rate(%).")

gross_pay = (int(hours)*int(pay_rate))
gp = round(gross_pay, 2)
contribution = float(CPF_rate)
contribution2 = contribution*0.01
contribution3 = round(contribution2*gp, 2)
net_pay = round(gross_pay - contribution3, 2)
print("Payroll statement for Mr/Mrs", name)
print("Number of hours that you worked in a week :", hours)
print("Your hourly pay rate is $" + pay_rate)
print("Your gross pay is $" + str(gp))
print("Your CPF contribution is $" + str(contribution3))
print("Lastly, your net pay is $" + str(net_pay))

