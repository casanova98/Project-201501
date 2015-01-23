
import binascii

answer = input("Type any whole number and I will print the ascii value that represent it.")

a = int(answer)

if 0<=a<=127:
    print(chr(a))
else:
    print("Try again.")

