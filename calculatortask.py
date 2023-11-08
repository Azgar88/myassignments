#calculator
while True:
    def add(x,y):
        return x+y
    def subtract(x,y):
        return x-y
    def multiply(x,y):
        return x*y
    def division(x,y):
        return x/y
    my_str=input("enter your option")
    x=int(input("enter number"))
    y=int(input("enter number"))
    if my_str=="1":
        print(add(x,y))
    elif my_str=="2":
        print(subtract(x,y))
    elif my_str=="3":
        print(multiply(x,y))
    elif my_str=="4":
        print(division(x,y))
    else:
        print("invalid option")
