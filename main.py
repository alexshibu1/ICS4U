print(
'''
Name: Alex Shibu 
Grade: 12
Descripion: A program calculates the total hours worked by an employee 
Date: October 12, 2021\n
''')

#requesting user input for hourse worked
userHour = int(input("Please enter the total hours worked this week: ") )

while userHour > 168:
  userHour = int(input("\nInvalid! Please enter the total hours worked this week: ") )
  
#Seting up variables
full_Time = 40

#processing and printing out how much they've made over the week
if userHour  <= 20:
  userPay = userHour * 9
  print("\nThis week you'll be paid $"+str(userPay), "for working",userHour, "hours part-time")
elif userHour  > 20 and userHour < full_Time:
  userPay = userHour * 10
  print("\nThis week you'll be paid $"+str(userPay), "for working",userHour, "hours full-time")
elif userHour  > full_Time and userHour < 168:
  userOv = userHour - full_Time
  userPay = full_Time * 10 + userOv * 15 
  print("\nThis week you'll be paid $"+str(userPay), "for working 40 hours full time and",userOv, "hours overtime  ")
