prices = [3,7,5,1,4,6,2,3]
def highest(prices):
    n = len(prices)
    best = 0
    for i in range(n):
        for j in range(i+1,n):
            best = max(best,prices[j]-prices[i])
    return best
def highest_improve(prices):
    n = len(prices)
    best = 0
    for i in range (n):
        minprices = min(prices[0:i+1])
        best = max(best,prices[i]-minprices)
    return best
def highest_bestimprove(prices):
    n = len(prices)
    minprices = prices[0]
    best = 0
    for i in range(n):
        minprices = min(minprices,prices[i])
        best = max(best,prices[i]-minprices)
    return best
print(highest_bestimprove(prices))
print(highest(prices))
print(highest_improve(prices))