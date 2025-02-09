listinteger = [1,-1,1,-1,1,-1,1,-1]
def SplitList(listinteger):
    n = len(listinteger)
    result=0
    for i in range(n-1):
        left_sum = sum(listinteger[0:i+1])
        right_sum=sum(listinteger[i+1:])
        if left_sum == right_sum:
            result +=1
    return result
def SplitList_Improve(listinteger):
    n = len(listinteger)
    left_sum=0
    result = 0
    total = sum(listinteger)
    for i in range(n-1):
        left_sum += listinteger[i]
        right_sum = total - left_sum
        if left_sum==right_sum:
            result+=1
    return result
print(SplitList(listinteger))
print(SplitList_Improve(listinteger))
