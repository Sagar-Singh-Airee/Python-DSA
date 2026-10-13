import math    #This is the lib that we should use if  we want to calculte fast
'''#This file is to  review pyhton !'''
my_list=["Sagar",10,20,30,44,55]
length=len(my_list)
print("The elment in your list are :-" , my_list)
print ("Lenght of my list is: ", length)

print("*"*50)


'''if we want to print a perticular element form this list we just have to use slicing or indexing'''
print("My first element in the list is : ", my_list[0])

print("*"*50)


'''Lets pop something out form the list'''
my_list.pop() #THis will remove the last element form the list.
my_list.pop(1) #This will pop the iteam in the list with the indexing of 1

print("*"*50)


'''Let's append an iteam now'''
my_list.append("kurama") #This will append a string named kurama to the end of the list
print("After the change my list is :- ", my_list)

print("*"*50)


'''And now if we want to insert an item in the middle or some other place this is how we do it '''
my_list.insert(0,44) #a_list.insert(i,item) Inserts an item at the ith position in a list
my_list.insert(2,55) #Now what it does is that, it shifts the existing no. one position ahead. here 20 was in the 2nd index but after inserting it is not in the 3rd index

print("*"*50)


'''If we want to see the list item one by one than!'''
for i in my_list:
    print(i)
    i=+1
print("[For] loop executed well")

print("*"*50)

'''If we want to reverse the order of the list then we also a specific funtion'''
my_list.reverse()
print(my_list)

print("*"*50)


'''If we want to return the first occurance of the item'''
print("Index of 44 in the new list : ", my_list.index(44))  #We have to use print if we want to see the index no. of this item

print("*"*50)



'''If we want to count the no. of occurance of an item then'''
print("No. of time 44 is been repeated : ", my_list.count(44))

print("*"*50)


'''Now understanding how range works'''
for j in range(0,10):
    print(j) #This will print all the whole no.s between 0 and 10 including 0 but not 10

print("*"*50)


'''Another format of range'''
for j in range(0,10,2): #This will start with '0' and give you the jumps of '2' till it reaches 9 which is done in range.
    print(j)

print("#"*50)   

'''Now lets use try and except'''
a_number=int(input("Please enter a number -->"))
try:
    print(math.sqrt(a_number))
except:
    print("This is the bad value for squre root")
    print("Try using a positive integer")
    print(math.sqrt(abs(a_number))) #abs is used to get the absolute value for if the number is negative then it will give positive value and if it is complex than it will give the magnitude





