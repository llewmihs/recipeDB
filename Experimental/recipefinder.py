# let's start by loading the recipe names from the filenamesin the database folder
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("database") if isfile(join("database", f))]

from itertools import cycle, islice, dropwhile

import gkeepapi

from creds import usr, pss

keep = gkeepapi.Keep()
success = keep.login(usr, pss)


# so this prints all files in this format ['recipe1'.txt,'recipe2.txt']
#print(onlyfiles)

# let's try and assign them to a dictionary so that I can call '1' as 'recipe1.txt'



# initiate the recipe list
rList = {}
# initiate the shopping list
sList = {}
# initiate a meals dict
meals = []
# initalise an index for the recipes
index = 1
# days of the week list
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat','Sun']
for items in onlyfiles:
    rList.update({index:items})
    index += 1

# set up the loop through the days of the week
startDay = input("What is the first day of your food week? Mon, Tue, Wed, Thu, etc.")
print()

#find the index of the start day
# this next bit reorders the days list for simple iteration through later
dIndex = days.index(startDay)
cycled = cycle(days)
skipped = dropwhile(lambda x: x != startDay, cycled)
sliced = islice(skipped, None, 7)
days = list(sliced)

print(rList)

for i in range(7):
    meal = int(input("What would you like to eat on %s ?   " % days[i]))
    # add the meal to a list of meals for the week
    meals.append(rList[meal])
    # now retrieve the ingredients for that meal
    path = str("database/" + rList[meal])
    lines = [line.rstrip('\n') for line in open(path)]
    for item in lines:
        split = item.split(';')
        if not split[0] in sList:
            sList[split[0]] = int(split[1])
        else:
            sList[split[0]] += int(split[1])

for i in range(7):
    print(days[i]+ "  " + meals[i])

print(sList)

keepTasks=[]

for items in sList:
    keepTasks.append((items + " " + str(sList[items]), False))

glist = keep.createList('Shopping List', keepTasks)
glist.pinned = True

keep.sync()

# print(keepTasks)