#ex-1
a=int(input("enter a number"))
if a%2==0:
    print("a is an even number")
elif a%3==0:
    print("a is an odd number")
else:
    print("a is invalid number")

#ex-2
score=int(input("Enter your score"))
if score>=90:
    print("your grade is A")
elif score>=75:
    print("Your grade is B") 
else:
    print("Your grade is C")

#ex-3
year=int(input("Enter Year"))
if year%4==0 and year%100!=0:
    print(year,"is a leap year")
elif year%400==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")                           