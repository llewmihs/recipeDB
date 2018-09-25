# let's start by loading the recipe names from the filenamesin the database folder
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("database") if isfile(join("database", f))]

# so this prints all files in this format ['recipe1'.txt,'recipe2.txt']
#print(onlyfiles)

# let's try and assign them to a dictionary so that I can call '1' as 'recipe1.txt'



# initiate the recipe list
rList = {}
# initiate the shopping list
sList = {}
# initalise an index for the recipes
index = 1
# days of the week list
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat','Sun']
for items in onlyfiles:
    rList.update({index:items})
    index += 1

# set up the loop through the days of the week
startDay = input("What is the first day of your food week? Mon, Tue, Wed, Thu, etc.")

#find the index of the start day
dIndex = days.index(startDay)

for i in range(7):
    dIndex = days.index(startDay)
    print(days[i])


print(rList)
choice = int(input("Which recipe would you like to add?  "))
#print(type(choice))
# How to return a recipe from a number
print(rList[choice])

# now i need to open the recipe
path = str("database/" + rList[choice])
# f = open(path,"r")

lines = [line.rstrip('\n') for line in open(path)]

# excellent i now have the ingredients in a list that looks
# like this ['chicken breast;4', 'butter;200', 'eggs;3', 'milk;300']

for item in lines:
    split = item.split(';')
    print(split)
    if not split[0] in sList:
        sList[split[0]] = int(split[1])
    else:
        sList[split[0]] += int(split[1])

print(sList)
