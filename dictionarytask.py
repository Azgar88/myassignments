# 1.Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
Sample_Dictionary = {0: 10, 1: 20}
my_key=2
my_value=30
Sample_Dictionary.update({my_key:my_value})
print(Sample_Dictionary)
# 2.Write a Python script to check whether a given key already exists in a dictionary.
my_dict = {1:"apple",2:"pineapple",3:"banana",4:"mango"}
checking_key = int(input("enter key"))
if checking_key in my_dict:
    print("exists in the dictionary.")
else:
    print("does not exist in the dictionary.")
# 3.Write a Python program to iterate over dictionaries using for loops
my_dict={1:"apple",2:"pineapple",3:"banana",4:"mango"}
for i,j in my_dict.items():
    print(f"{i}:{j}")
# 4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
my_dict={i:i**2 for i in range(1,16)}
print(my_dict)
# 5.Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'marolix technology'
# Expected output: {'m': 1, 'a': 1, 'o': 3, 'l': 2, 'i': 1, 'x': 1, 't': 1, 'e': 1,'c': 1, 'h': 1, 'n': 1, 'g': 1,'y':1}
my_dict={}
Sample_string='marolix technology'
for i in Sample_string:
    if i.isalpha():
        i=i.lower()
        if i in my_dict:
            my_dict[i]+=1
        else:
            my_dict[i]=1    
for i,j in my_dict.items():
    print(f"{i}:{j}")
# 6. Write a Python program to sum all the items in a dictionary.
my_dict={1:10,2:20,3:30,4:40,5:50}
my_sum=0
for i in my_dict.values():
    my_sum+=i
print(my_sum)
# 7.Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
from collections import Counter
my_dict=Counter(d1)+Counter(d2)
print(my_dict)
# 8.Write a Python program to access dictionary key's element by index.
# Expected Output:
# physics
# math
# chemistry
my_dict={"sub1":"physics","sub2":"math","sub3":"chemistry"}
for i in my_dict.values():
    print(i)
# 9.Write a Python program to remove a key from a dictionary.
my_dict={1:"java",2:"c++",3:"devops",4:"python"}
my_dict.pop(2)
print(my_dict)
# 10.Write a Python script to merge two Python dictionaries
dict_1={"Name":"Tom","Age":"30"}
dict_2={"City":"New York","Country":"USA"}
dict_1.update(dict_2)
print(dict_1)
