#1 write a python program to remove a given character from string
str = input("enter a string")
char = input("enter a char")
print(str.replace(char,""))

#2 write a program to check string is palindrome or not
str = input("enter string")
palindrome_str=str[::-1]
if str == palindrome_str:
    print("string is palindrome")
else:
    print("string is not palindrome")

#3 write a python program to check given character is vowel or consonant
my_char = input("enter a char")
if my_char in "aeiouAEIOU":
    print("is a vowel")
else:
    print("is a consonent")

#4 write a python program to replace string space with given character in python
str=input("enter a str")
my_char=input("enter char")
print(str.replace(" ",my_char))

#5 write a python program to count aplhabets,digits and special characters in the string.
my_str=input("enter a string")
alphabets=0
digits=0
special_characters=0
for i in my_str:
    if i.isalpha():
        alphabets+=1
    elif i.isdigit():
        digits+=1
    else:
        special_characters+=1
print("alphabets are : ",alphabets)
print("digits are : ",digits)
print("sepcial characters are : ",special_characters)

#6 write a python program to remove all th blank spaces in a given string 
str=input("enter string")
print(str.replace(' ',''))

#7 write a python program to find sum of interegers in string
my_str=input("enter string")
sum=0
for i in my_str:
    if i.isdigit():
        sum=sum+int(i)
print(sum)        

#8 write a python program to remove repeated characters from string
str=input("enter a string")
my_str=" "
for i in str:
    if i not in my_str:
        my_str=my_str+i
print(my_str)        

#9 write a python program to count occurance of given character in string
my_str=input("enter a string")
my_char=input("enter a character")
print(my_str.count(my_char))

#10 write a python program to check string is anagrams or not in python
str_1=input("enter a string")
str_2=input("enter a string")
if len(str_1)!=len(str_2):
    print("string is not an anagram")
elif sorted(str_1) == sorted(str_2):
    print("string is an anagram")
else:
    print("string is not an anagram")    

