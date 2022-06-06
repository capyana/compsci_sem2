length=int(input("Please enter line length"))
width=int(input("Please enter the width"))
height=int(input("Please enter a height"))
symbol=str(input("Input a character"))
for y in range(height):
    for x in range(width):
        print(symbol, end= "")
    print("")
