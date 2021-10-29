print(
'''
Name: Alex Shibu 
Grade: 12
Descripion: A program that determine when the population exceeds its food supply.  
Date: October 28, 2021\n
''')

numAnimals = 10;
numFood = 1000
boolean = False
cntHour = 0 
while boolean == False:
  numFood = numFood + 4000
  cntHour = cntHour  + 1
  numAnimals = numAnimals * 2
  if numAnimals > numFood:
    print("The number of food available for animals have exceeded the population of the animals at", cntHour, "hours" ) 
    boolean = True