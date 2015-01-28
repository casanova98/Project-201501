

answer_1 = input("Enter the length of the first side of a triangle.")
answer_2 = input("Enter the length of the second side of a triangle")
answer_3 = input("Enter the length of the third side of a triangle")

side_1 = int(answer_1)
side_2 = int(answer_2)
side_3 = int(answer_3)

total_side = side_1 + side_2 + side_3

def triangle_formula():

    if side_1 + side_2 <= side_3:
        return False

    elif side_1 + side_2 > side_3:
        return True

    if side_2 + side_3 < side_1:
        return False

    elif side_2 + side_3 > side_1:
        return True

    if side_1 + side_3 < side_2:
        return False

    elif side_1 + side_3 > side_2:
        return True

if triangle_formula() == False:
    print("Invalid Triangle!")
elif triangle_formula() == True:
    print("Perimeter of triangle is", total_side)