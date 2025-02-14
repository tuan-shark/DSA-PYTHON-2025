"""  
You are given a list of numbers. How many distinct numbers does it contain?  

For example, when the list is [3, 1, 2, 1, 5, 2, 2, 3], the desired answer is 4, because the distinct numbers are 1, 2, 3 and 5.
"""
#solve use list
numbers = [3,1,2,1,5,2,2,3]
mylist = []
myset = set()
def solve(numbers):
    for number in numbers:
        if number not in mylist:
            mylist.append(number)
    return len(mylist)
print(solve(numbers))
# extreamly good but the complexity is bad ==> O(n^2) ==> because not in function is O(n) 
#solve use set
def solve1(numbers):
    for number in numbers:
        if number not in myset:
            myset.add(number)
    return len(myset)
print(solve1(numbers))
#shorter way 
print(len(set(numbers)))