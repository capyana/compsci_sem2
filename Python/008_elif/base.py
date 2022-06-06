x=int(input("Enter your first number"))
y=int(input("Enter your second number"))
z=str(input("What operation would you like to complete?*, /, +, or -"))
if(z=="*"):
    print(x*y)
elif(z=="/"):
    print(x/y)
elif(z=="+"):
    print(x+y)
elif(z=="-"):
    print(x-y)