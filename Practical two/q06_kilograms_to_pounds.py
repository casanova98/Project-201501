

print("\t".join(["Kilograms", "Pounds"]))

def converter(n):
    pounds = round((n*2.2), 2)
    print("%s \t\t\t %s" % (n, pounds))

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for number in x:
    number = int(number)
    converter(number)