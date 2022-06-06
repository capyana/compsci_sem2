x=int(input("How many items would you like to buy?"))
total_cost=0
for x in range(0,int(x)):
    y=str(input("What item are you purchasing?"))
    z=int(input("How much is the item?"))
    print("Thank you for purchasing "+str(y)+"!")
    total_cost += z
print(f"Your total is ${total_cost}!")
