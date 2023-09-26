#1 write a python program to merge two lists.
#approach1
list_1=["apple","banana","cranberry"]
list_2=["strawberry","mango","oranges"]
list_3=list_1+list_2
print(list_3)

#approach2
list_1=["apple","banana","cranberry"]
list_2=["strawberry","mango","oranges"]
list_1.extend(list_2)
print(list_1)

#2 write a python program to find the sum of list elements.
#approach1
my_list = [10,20,30,40,50]
sum_of_list=sum(my_list)
print(sum_of_list)

#approach2
my_list = [10,20,30,40,50]
sum = 0
for i in my_list:
    sum+=i
print("sum of elements is:",sum)

#3.write a python program to print even and odd numbers seperatly in list.
#approach1
my_list=[1,2,3,4,5,6]
odd_list=[i for i in my_list if i%2!=0]
print(odd_list)
even_list=[i for i in my_list if i%2==0]
print(even_list)

#approach2
my_list=[1,2,3,4,5,6]
even_list=[]
odd_list=[]
for i in my_list:
    if i%2!=0:
        odd_list.append(i)
    else:
        even_list.append(i)
print(odd_list)
print(even_list)            

#4.write a python program to delete element of given index in list.
#approach1
my_list=["apple","banana","mango","orange"]
del_index=int(input("enter index number"))
my_list.pop(del_index)
print(my_list)

#5.write a python program to delete given elemet from the list
#approach1 
my_list=["apple","banana","mango","orange"]
del_index=input("enter element")
my_list.remove(del_index)
print(my_list)

#approach2
my_list=["apple","banana","mango","orange"]
del_element=input("enter element")
new_list=[i for i in my_list if i.strip(del_element)]
print(new_list)

#6.write a python program to insert an elemet  at given index location.
#approach1
my_list=["apple","banana","mango","orange"]
insert_element=input("enter element")
insert_position=int(input("enter index position"))
my_list.insert(insert_position,insert_element)
print(my_list)

#7.write a python program to check the sizes of given two lists are same.
#approach1
list_1=input("enter list").split(',')
list_2=input("enter list").split(',')
if len(list_1)==len(list_2):    
    print("sizes of given two lists are same")
else:
    print("sizes of given two lists are not same")

#8.Write a Python function that takes two lists and returns True if they have at least one common member.
list_1=[1,2,3,4,5]
list_2=[5,6,7,8,9]
for i in list_1:
    if i in list_2:
        break
if i in list_2:
    print("true")
else:
    print("false")

#Write a Python program to remove a specified column from a given nested list.
#Original Nested list:[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
#approach1
Original_Nested_list=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
my_list=[]
for i in Original_Nested_list:
    i.pop(0)
    my_list.append(i)
print(my_list)

# 9.Write a Python program to convert a list of multiple integers into a single integer.
#   Sample list: [11, 33, 50]
#   Expected Output: 113350
#approach1
sample_list=[11,33,50]
output=" "
for i in sample_list:
    output+=str(i)
output_int=int(output)
print(output_int)

#10.Write a Python program to remove duplicates from a list.
#approach1					
my_list=[1,1,2,2,3,3,4,4,5,5]
remove_duplicates=list(set(my_list))
print(remove_duplicates)

#appeoach2
original_list=[1,1,2,2,3,3,4,4,5,5]
remove_duplicates=[]
for i in original_list:
    if i not in remove_duplicates:
        remove_duplicates.append(i)
print(remove_duplicates)
