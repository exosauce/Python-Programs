def median (lst):
    l = len(lst)
    slst = sorted(lst)
    m=l//2
    if l%2==0:
        x=float(slst[m]+slst[m-1])/2
        return x
    else:
        return float (slst[m])
        
def addTwo (lst):
    newLst = []
    for i in range(0, len(lst),2):
        #print(str(i),end=', ')
        if i+1 < len(lst):
            x = lst[i] + lst[i+1]
        else:
            x = lst[i]
            
        newLst.append(x)
    return newLst

def addTwoSlice(lst):
    newLst = []
    for i in range(0, len(lst),2):
        shortList = lst[i:i+2]            
        newLst.append(sumLst(shortList))
    return newLst


def sumLst(lst):
    x = 0
    for i in range(0, len(lst)):
        x = x+lst[i]
    return x
