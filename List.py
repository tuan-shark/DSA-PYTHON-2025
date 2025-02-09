"""
List in memory 
example:
a = 7
b = -3
c = [1, 2, 3, 1, 2]
d = 99
100	101	102	103	104	105	106	107	108	109	110 addresses
7	-3	1	2	3	1	2	0	0	0	99 values
a	b	c	 	 	 	 	 	 	 	d variables
The ways list save the varibles is by adding the element index of the element we want to access
like c[2] : the address is 102 + 2 = 104
List have 2 seprate size 
The first is : logical size :
like in list c we have logical size is 5 
second is capacity : more than 5 can not know exact because is from computer

"""
#list operations
#1.INDEXING
numbers = [4,3,7,3,2]
print(numbers[2])
#numbers[2]=99
print(numbers[2])
# complexity to do this is O(1) we only do 1 work to do this
#2.List size
print(len(numbers))
#complexity to do this is O(1)
#3.SEARCHING
print(3 in numbers) #TRUE ==> 3 is in the list
print(8 in numbers)#false ==> 8 is not in the list
print(numbers.index(7)) #==> return to the position the number 3 is first appeare ==> 1
print(numbers.count(3)) #==> count the frequency of number 3 ==> 2
#Complexity is O(n) ==> need to loop through list
#4.ADDING AN ELEMENT
numbers1 = [1,2,3,4]
#append is add to the end of the list
numbers1.append(5)
#Complexity : O(1)
print(numbers1)
#insert is add to the given position
numbers1.insert(0,0)
print(numbers1)
#Complexity : O(n)
#5.Removing an element
numbers2 = [1,2,3,4,5,6]
numbers2.pop()
print(numbers2) # [1, 2, 3, 4, 5]
numbers2.pop(1)
print(numbers2) # [1, 3, 4, 5]
#if the pop the last ==> complexity is O(1)
#if not the last ==> all another position is O(n)
#Another way to remove element
numbers3 = [1, 2, 3, 1, 2, 3]

numbers3.remove(3)
print(numbers3) # [1, 2, 1, 2, 3]
#this function will remove the 3 but in the first position this number appeare
#Complexity: O(n)
#6.REFERENCE AND COPYING
a = [1, 2, 3, 4]
b = a
a.append(5)
print(a) # [1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4, 5]
#==> this is copying
#like a and b is "connect" with the same list in memory
#6.REFERENCE AND COPYING
a = [1, 2, 3, 4]
b = a
a.append(5)
print(a) # [1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4, 5]
#==> this is copying
#like a and b is "connect" with the same list in memory
#6.REFERENCE AND COPYING
a = [1, 2, 3, 4]
b = a
a.append(5)
print(a) # [1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4, 5]
#==> this is copying
#like a and b is "connect" with the same list in memory
a = [1, 2, 3, 4]
b = a.copy()
a.append(5)

print(a) # [1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4]
#==>this in refer
#like b is refer to the separate list and anything done with a is not relate with b
#Slicing and concatenation
numbers6= [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers6[2:6]) # [3, 4, 5, 6] shift to pos 2 to pos 5
#Complexity : O(n)
first = [1, 2, 3, 4]
second = [5, 6, 7, 8]
print(first + second) # [1, 2, 3, 4, 5, 6, 7, 8]
#Complexity : O(n) ==> because is need to copy the element and add to new list

