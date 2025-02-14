"""
hashing is a special technique 
hashing techinque have 2 special values:
keys - values
ex : 1 - " apple"
2 - "banana"
special is here : pairs key - value can not be duplicate
so ==> we can use this to solve some exercises to find pairs and dont need to wory about duplicate
In python : we have 2 built in data structure which using hashing
SET AND DICT(DICTIONARY)
"""
#SET
"""
DIFFERENT WITH LIST SET CAN NOT BE ACCESS THROUGH INDEX BECAUSE SET DOES NOT SAVE VALUES NEXT TO LIKE IN LIST
TAKE AN EXAMPLE:
THIS IS HOW LIST SAVE
a = 7
b = -3
c = [1, 2, 3, 1, 2]
d = 99
100	101	102	103	104	105	106	107	108	109	110 addresses
7	-3	1	2	3	1	2	0	0	0	99 values
a	b	c	 	 	 	 	 	 	 	d variables
==> IN LIST WE CAN ACCESS LIKE C[2] = ADDRESS 102 + 2 == > ADDRESS 104 : VALUES : 3
BUT SET LIKE I JUST WRITE BEFORE USE HASHING
Address	Value
200	10
208	-3
215	5
220	7
234	2
IT SAVE RANDOM SO WE CAN NOT USE INDEX TO FIND WE CAN ONLY FIND VALUES THROUGH KEY 
LIKE PRINT(DICT("APPLE")) ==> RETURN THE KEYS CONNECT WITH STRING APPLE
"""
#example for set
numbers = set()
numbers.add(1)
numbers.add(2)
numbers.add(3)
print(numbers)
#operation and complexity in list and set:
# Operation	List and Set
"""
LIST ......... SET .............Complexity of list.............Complexity of set
append          add                    O(1)                         O(1)
IN and NOT IN    IN And Not in         O(n)                         O(1)
remove             remove              O(n)                         O(1)
"""
