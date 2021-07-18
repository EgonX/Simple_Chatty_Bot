def valid_triagle(a, b, c):
    if int(a) + int(b) + int(c) == 180:
        message = ""
    else:
        message = " not"
    print("The triangle is" + message + " valid!")

side1 = input()
side2 = input()
side3 = input()

valid_triagle(side1, side2, side3)
