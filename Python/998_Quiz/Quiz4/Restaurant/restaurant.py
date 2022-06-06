import random

resturants =["Seasoning Alley","Jersey Mike's","The Habit"]
SeasoningAlley=["Kebab","Shawarma","Dolma"]
JerseyMikes=["Sandwich","Mike's way","Chips"]
TheHabit=["Double barbeque bacon charburger","Salted caramel malt","Onion rings"]

resturants = resturants[random.randrange(0,3)]
print("The resturants is "+resturants)

if resturants =="Seasoning Alley":
    item = SeasoningAlley[random.randrange(0,3)]
    print("The menu item is "+ item)
    
elif resturants =="Jersey Mike's":
    item= JerseyMikes[random.randrange(0,3)]
    print("The menu item is"+ item)
    
elif resturants =="The Habit":
    item= TheHabit[random.randrange(0,3)]
    print("The menu item is"+ item)