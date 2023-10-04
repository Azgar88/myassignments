#1.Write a Python program to unpack a tuple into several variables
my_tuple=("apple","banana","mango","ornage")
tup1,tup2,tup3,tup4=my_tuple
print(tup1)
print(tup2)
print(tup3)
print(tup4)

#2.Write a Python program to add an item to a tuple.
#approach1
my_tuple=("apple","banana","orange","kiwi")
my_item=input("enter item")
tup_list=list(my_tuple)
tup_list.append(my_item)
print(tuple(tup_list))

#approach2
my_tuple=("apple","banana","orange","kiwi")
tup_list=list(my_tuple)
my_item=input("enter item")
my_position=int(input("enter position"))
tup_list.insert(my_position,my_item)
print(tuple(tup_list))

#3.Write a Python program to convert a tuple to a string.
#Ex:tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
my_str = ''.join(tup)
print(my_str)

#4.Write a Python program to get the specified element from the last element of a tuple.
my_tup=("apple","banana","pineapple","mango","orange")
my_index=int(input("enter index position"))
my_tupindex=int(input("enter index position"))
print(my_tup[my_index][my_tupindex])

#5.Write a Python program to add member(s) to a set.
#approach1
my_set={"apple","banana","mango"}
my_list=list(my_set)
add_item=input("enter item")
my_list.append(add_item)
print(set(my_list))

#approach2
my_set={"apple","banana","mango"}
add_item=input("enter item")
my_set.add(add_item)
print(my_set)

#6.Write a Python program to create an intersection of sets.
my_set1={10,20,30,40,50}
my_set2={30,50,60,70,80}
print(my_set1&my_set2)
print(my_set1.intersection(my_set2))

#7.Write a Python program to create a union of sets.
my_set1={"10","20","30","40","50"}
my_set2={"60","70","80","90","100"}
print(my_set1.union(my_set2))
print(my_set1|my_set2)

#8.Write a Python program to create set difference.
my_set1={10,20,30,40,50}
my_set2={30,50,60,70,80}
print(my_set1.difference(my_set2))
print(my_set1-my_set2)

#9.Write a Python program to create a symmetric difference.
my_set1={10,20,30,40,50}
my_set2={40,50,60,70,80}
print(my_set1.symmetric_difference(my_set2))
print(my_set1^my_set2)

#10.Write a Python program to find the maximum and minimum values in a set.
my_set={10,20,30,40,50}
print(max(my_set))
print(min(my_set))