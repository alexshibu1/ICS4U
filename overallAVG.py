
print(
'''
Name: Alex Shibu 
Grade: 12
Descripion: A program orders three integers from lowest to highest 
Date: October 27, 2021\n
''')

intGrade = 0
total = 0
countvul = 0
boolen = True

while boolen == True and int(intGrade) >= 0 and int(intGrade) <= 100:
  intGrade = input("Please Input Grades(Exit = e): ")

  if str(intGrade) == "e":
    boolen = False

  elif int(intGrade) >= 0 and int(intGrade) <= 100:
    total = total + int(intGrade)
    countvul = countvul + 1
    ovAverage = total // countvul


print("\nOverall average:",ovAverage,"%")
