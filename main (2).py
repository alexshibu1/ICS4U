
print('''
Name: Alex Shibu 
Grade: 12
Descripion: A program calculates the area and perimeter of a rectangle
Date: October 11, 2021
''')
#requesting user input for height of the rectangle
userH = int(input("Please enter the height of the rectangle: ") )

#requesting user input for width of the rectangle
userW = int(input("Please enter the width of the rectangle: ") )

#Calculates the area of the rectangle
area = userH * userW

#prints the area of the rectangle
print("The area of the rectangle is", area, "m^2")

#Calculates the perimeter of the rectangle
perimeter = userH *2 + userW*2

#prints the perimeter of the rectangle
print("The perimeter of the rectangle is", perimeter, "m")

