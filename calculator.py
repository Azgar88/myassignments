def calculator():
    while True:
        my_str=input("enter your option")
        for i in my_str:
            if i=="1":
                a=int(input("enter number"))
                b=int(input("enter number"))
                print(a+b)
            elif i=="2":
                a=int(input("enter number"))
                b=int(input("enter number"))
                print(a-b)
            elif i=="3":
                a=int(input("enter number"))
                b=int(input("enter number"))
                print(a*b)
            elif i=="4":
                a=int(input("enter number"))
                b=int(input("enter number"))
                print(a/b)
            else:
                print("not a valid option")
calculator()