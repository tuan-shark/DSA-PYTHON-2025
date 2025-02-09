bits = [0,1,0,0,1,0,1,1]
def FindBits(bits):
    n = len(bits)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if bits[i] == 0 and bits[j]==1:
                count +=1
    return count
def FindBits_improve(bits):
    n = len(bits)
    zeros = 0
    result = 0
    for i in range(n):
        if bits[i] == 0:
            zeros +=1
        if bits[i] == 1:
            result +=zeros
    return result
print(FindBits(bits))
print(FindBits_improve(bits))

                    