from random import choice

resChoice = ['Burgers', 'Other', 'Asian', 'Cafe Style', 'Mexican', 'Pizza', 'Sandwiches', 'Chicken']


burgers = ['Wendys', 'Burger King', 'McDonalds', 'A&W', 'Sonic', 'Cook Out', 'Steak n Shake', 'Culvers', 'White Castle', 'Arbys']
other = ['Fazolis', 'Masala']
asian = ['Thai Smile', 'Tsing Tao', 'Noodle Shack', 'Panda Express', 'Khins Sushi']
cafe = ['Panera', 'Starbucks', 'Dunkin Donuts', 'McAlisters Deli', 'Purdys']
mexican = ['Qdoba', 'Taco Bell', 'Don Senor', 'Hidalgo']
pizza = ['Dominos', 'Little Caesers', 'Papa Johns', 'Mad Mushroom']
sandwich = ['Jimmy Johns', 'Firehouse Subs', 'Subway', 'Penn Station']
chicken = ['Canes', 'Chick-fil-a', 'Zaxbys', 'KFC', 'Lees']

print("Do you want to pick the food type or have the generator pick for you?")
print("------------------------")
print("1. Pick for me")
print("2. I want to pick")
print("------------------------")
decision = int(input("Type 1 or 2: "))

if decision == 1:
    resType = choice(resChoice)
    resNum = 0
    print("We chose "+resType+".")

elif decision == 2:
    print("What type of food would you like for us to choose from?")
    print("------------------------")
    print("1. Burgers")
    print("2. Asian")
    print("3. Cafe Style")
    print("4. Mexican")
    print("5. Pizza")
    print("6. Sandwiches")
    print("7. Chicken")
    print("8. Other")
    print("------------------------")
    resNum = int(input("Type the number you would like to select: "))
    resType = ""
else:
    print("You are stupid, that is not 1 or 2.")
    resType = ""
    resNum = 0


if resType == 'Burgers' or resNum == 1:
    print("You will be eating: "+choice(burgers))
elif resType == 'Other' or resNum == 8:
    print("You will be eating: "+choice(other))
elif resType == 'Asian' or resNum == 2:
    print("You will be eating: "+choice(asian))
elif resType == 'Cafe Style' or resNum == 3:
    print("You will be eating: "+choice(cafe))
elif resType == 'Mexican' or resNum == 4:
    print("You will be eating: "+choice(mexican))
elif resType == 'Pizza' or resNum == 5:
    print("You will be eating: "+choice(pizza))
elif resType == 'Sandwiches' or resNum == 6:
    print("You will be eating: "+choice(sandwich))
elif resType == 'Chicken' or resNum == 7:
    print("You will be eating: "+choice(chicken))
#
#
#
#
#
#
