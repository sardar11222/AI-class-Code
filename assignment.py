import time
t=time.localtime(time.time())
localtime=time.asctime(t)
str="Current Time: " + time.asctime(t)
print(str)

# Question 1
A="5"
B="6"
C=int(A)+int(B)
print(C)

x = 5
print(type(x))
y="Hello!"
print(type(y))



# question 2
Marks=[87,45,67,89,98]
print(Marks)
print("Length of list ", len(Marks))

my_list=[12,34,56,78]
# use of loop to iterate over my_list
print("My list: ")
for i in my_list:
    print(i)
# Access elements by use of indexing or slicing
print("3rd element of my_list is", my_list[2])
print("Get a subset of my list (Slicing)")
my_list[1:4]
print("Add item to the List")
# Add element to list
my_list.append(67)
print(my_list)
# remove element from a list
print("Remove item from a List")
my_list.remove(78)
print(my_list)
# sort a list
print("Sorted list")
my_list.sort()
print(my_list)
# copy A list
print("Copy a list")
copy=my_list.copy()
print(copy)

my_list=[1,2,3,4,5]
print("Original list:", my_list)
square=[i*i for i in my_list] # List comprehension 
print("Square of List:", square)



# question 3
# Accessing tuple elements
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  
print(my_tuple[-1])  

# looping through a tuple
my_tuple = (1, 2, 3, 4, 5)
for I in my_tuple:
    print(I)

# updating a tuple
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_list[0] = 10
my_tuple = tuple(my_list)
print(my_tuple) 

# unpacking a tuple
my_tuple = ("Apple","Banana","orange")
a,b,c=my_tuple
print(a)
print (b)
print (c)

# tuple methods
tup=(2,1,3,1)
print(tup.index(1))
print(tup.count(1))


# question 4
Numbers={1,2,3,4,5,6}
# Add element
print("Original set: ",Numbers)
Numbers.add(7) 
print("After adding: ", Numbers)
# remove element
print("Original set: ",Numbers)
Numbers.remove(5) 
print("After removing: ", Numbers)
# clear set
print("Original set: ",Numbers)
Numbers.clear() 
print("After clearing: ", Numbers)
# set pop
print("Original set: ",Numbers)
Numbers.pop() 
print("After pop: ", Numbers)
#union and intersection of two sets
S1={1,2,3,4} 
S2={3,4,5,6,7} 
Union=S1.union(S2) 
print(Union)
Intersection=S1.intersection(S2) 
print(Intersection)  



# question 5
import numpy as np
print("NumPy array")
arr = np.array([1, 2, 3, 4, 5])
print(arr) 
print("Basic operations")
print(arr + 2)  
print(arr * 2)  

import array
print("Array")
arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)
print("Basic operations")
arr.append(6)
print(arr)


# question 6
print("Initial list")
shopping_list = ["milk","bread","eggs","butter","juice","sugar","salt","biscuits","tea","coffee"]
for items in shopping_list:
    print(items)

add_item=input("Do you want to add new item? ") 
if add_item.lower()=="yes":  
    new_item=input("Enter new item: ")
    shopping_list.append(new_item)   
    print(new_item, "is added in the list")

remove_item=input("Do you want to remove item (yes/no) ")
if remove_item.lower=="yes":
    item_to_remove=input("Enter item to remove: ")
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
    else:
       	print("Item not found")   

print("Updated list")
for items in shopping_list:
    print(items)


# question 7
num=int(input("Enter a number: "))
def check_even_odd(num):
    if num%2==0:
        print(num, "is even number")
    else:
        print(num, "is odd number ")
        
check_even_odd(num)


# question 8
import pyjokes
Joke=pyjokes.get_joke()
print(Joke)

import random
# generate a random number between 1 to 10
print(random.randint(1,10))


# question 9
student_marks=(76,89,79,81,90,100) # tuple
#print first and last number of tuple 
print("First element of tuple is ", student_marks[0])
print("Last element of tuple is ", student_marks[-1])

#unpacking tuple 
print("Unpacked tuple ")
m1,m2,m3,m4,m5,m6=student_marks
print(m1)
print(m2)
print(m3)
print(m4)
print(m5)
print(m6)

new_tuple=list(student_marks)
for i in range(len(new_tuple)):
    new_tuple[i]+=5
new_tuple=tuple(new_tuple)

print("Original tuple")
print(student_marks)
print("New tuple")
print(new_tuple)


# question 10
numbers = [5, 12, 7, 18, 9, 24, 3, 16, 11]
divisible_by_3 = 0
even_not_divisible = 0
odd_not_divisible = 0
for num in numbers:
    if num % 3 == 0:
        print(num," is divisible by 3")
        divisible_by_3 += 1
    elif num % 2 == 0:
        print(num," is even but not divisible by 3")
        even_not_divisible += 1
    else:
        print(num," is odd and not divisible by 3")
        odd_not_divisible += 1
print("Numbers divisible by 3: ", divisible_by_3)
print("Numbers even but not divisible by 3: ", even_not_divisible)
print("Numbers odd and not divisible by 3: ", odd_not_divisible)


# question 11
def classify_numbers(numbers):
    counts = {"positive": 0, 
              "zero": 0, 
              "negative": 0}
    for num in numbers:
        if num > 0:
            print(num, " is positive")
            counts["positive"] += 1
        elif num == 0:
            print(num," is zero")
            counts["zero"] += 1
        else:
            print(num," is negative")
            counts["negative"] += 1
    return counts

numbers = [5, -3, 0, 2, -1, 0, 4, -2]
result = classify_numbers(numbers)
print("Counts:")
print("Positive: ", result['positive'])
print(f"Zero: {result['zero']}")
print(f"Negative: ",result['negative'])












