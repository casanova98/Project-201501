
answer = input("Enter your radius!")
radius = float(answer)

from math import pi

area = radius * radius * pi

print("This is the area to one decimal place ", round(area, 1))

answer_1 = input("Enter your length!")

b = float(answer_1)

volume = area * b

print("This is your volume to one decimal place ", round(volume, 1))