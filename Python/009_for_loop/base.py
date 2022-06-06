x=int(input("Please enter line length"))
z=str(input("Please enter a character"))
y=str.lower(input("Do you want a horizontal or vertical line?"))
if(y==("vertical")):
    for x in range (0,int(x)):
        print(z)
elif(y=="horizontal"):
        for x in range (0,int(x)):
            print(z, end=",")