#break
fruits = ["Apple","Banana","Mango","Pineapple","Watermelon"]
my_fruit = input("enter fruit name")
for i in fruits:
    if i==my_fruit:
        print("found!")
        break
    else:
        print("not found!")


#pass
for i in range(5):
    if i==3:
        pass
    print(i)


#continue
for i in range(1,11):
    if i%2 == 0:
        continue
    print(i)    