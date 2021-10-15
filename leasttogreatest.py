print(
'''
Name: Alex Shibu 
Grade: 12
Descripion: A program orders three integers from lowest to highest 
Date: October 12, 2021\n
''')


#requesting user input for integer values
int1 = int(input("Please enter integer 1: ") )

int2 = int(input("\nPlease enter integer 2: ") )

int3 = int(input("\nPlease enter integer 3: ") )


#Processing inputs and printing the lowest integer
if (int1 >= int3) and (int2 >= int3):
  value1 = int3
  print("\n\nIntegers ordered from least to greatest is\n",value1, ",",end=" ")
elif (int3 >= int2) and (int1 >= int2):
  value1 = int2
  print("\n\nIntegers ordered from least to greatest is\n",value1, ",",end=" ")
elif (int2 >= int1) and (int3 >= int1):
  value1 = int1
  print("\n\nIntegers ordered from least to greatest is: \n",value1, ",",end=" ")

#Processing inputs and printing an integer which is not the greatest nor the least
if (int1 <= int3 ) and (int2 >= int3):
  value2 = int3
  print (value2, ",",end=" ")
elif (int3 <= int2 ) and (int1 >= int2):
  value2 = int2
  print (value2, ",",end=" ")
elif (int2 <= int1 ) and (int3 >= int1):
  value2 = int1
  print (value2, ",",end=" ")

elif (int2 < int3 ) and (int1 >= int3):
  value4 = int3
  print (value4, ",",end=" ")
elif (int1 <= int2) and (int3 >= int2):
  value5 = int2
  print(value5, ",",end=" ")
elif (int3 <= int1 ) and (int2 >= int1):
  value6 = int1
  print (value6, ",",end=" ")

#Processing inputs and printing the greatest integer
if (int1 <= int3) and (int2 <= int3):
  value3 = int3
  print(value3)
elif (int3 <= int2) and (int1 <= int2):
  value3 = int2
  print(value3)
elif (int2 <= int1) and (int3 <= int1):
  value3 = int1
  print(value3)
