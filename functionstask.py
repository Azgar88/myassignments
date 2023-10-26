# 1.Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def upper_lower_count(my_str):
    uppercase_count=0
    lowercase_count=0
    for i in my_str:
        if i.isupper():
            uppercase_count+=1
        elif i.islower():
            lowercase_count+=1
    return uppercase_count,lowercase_count
my_str="The quick Brow Fox"            
uppercase_count,lowercase_count=upper_lower_count(my_str)            
print("No. of Upper case characters:",uppercase_count)
print("No. of Lower case characters:",lowercase_count)

# 2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def my_list(sample_list):
    i1=set(sample_list)
    i2=list(i1)
    print("unique list is:",i2)
sample_list=[1,2,3,3,3,3,4,5]
my_list(sample_list)

# 3.Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog".
def check_pangram():
    my_str=input("enter string")
    my_alphabets='abcdefghijklmnopqrstuvwxyz'
    for i in my_alphabets:
        my_str.lower()
    if i in my_str.lower():
        print("string is pangram")
    else:
        print("string is not pangram")        
check_pangram()

# 4.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10 (both included).
def list_of_squares(squares):
    for i in range(1, 11):
        squares.append(i*i)
    return squares
squares=[]
squares_list=list_of_squares(squares)
print(squares_list)

# 5.Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
def sum_of_list(number):
    emp_list = 0
    for i in number:
        emp_list+=i
    return emp_list
mylist=[8,2,3,0,7]
number=sum_of_list(mylist)
print(number)

#6.write a function to find sum of given values, pass values has variable number of arguments to function.
def sum_of_values(*x):
    total=sum(x)
    return total
addition_of_values=sum_of_values(1,2,3,4,5)
print(addition_of_values)