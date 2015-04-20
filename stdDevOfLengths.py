import math

def stdDevOfLengths(l):
    if not l:
        return float('NaN')
    
    lstLen = []
    for item in l:
        lstLen.append(len(item))
    
    total = float(sum(lstLen))
    mean = total/len(lstLen)
    print mean
    var = 0
    
    for item in lstLen:
        var += math.pow((item - mean),2)
    
    sd = math.pow(var/len(lstLen),0.5)
    return sd

#print stdDevOfLengths([])
#print stdDevOfLengths(['a', 'z', 'p'])
print stdDevOfLengths(['dw', 'hkcymdmsiudox'])
#print stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])
    