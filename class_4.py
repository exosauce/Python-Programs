def isPrimeNumber (n):
    x=2

    while x<n:
        if n%x == 0: 
            return False
        x = x + 1

    return True

#find the distance between next prime
#given 13, next is 14 no, 15 no, 16 no 17 Yes
def findNextPrime(n):
    while not isPrimeNumber(n+1):
        n=n+1
        
    return n+1
    
    
# givne 13,  13+2 = 15? prime? NO, 13-2=11 Prim? Yes. 13 has twin named 11
#1. if the given number not prime then return false
#2. 
def hasTwin(n):
    if not isPrimeNumber(n):
        return False
    if isPrimeNumber(n-2):
        return True
    if isPrimeNumber(n+2):
        return True
    return False

def findPrevPrime(n):
    while not isPrimeNumber(n-1):
        n=n-1

    return n-1


def starTriangleDown(n):
    i = 0

    while n > 0:
        while (i < n):
            print('*', end = ' ');
            i = i+1
        print()
        i = 0
        n = n -1
        
#challenge for you
def starTriangleUp(n):
    n += 1
    for i in range(1, n):
        print('* '*i)
       
        

def increaseAge(ages):
    i = 0
    while i < len(ages):
        ages[i] = ages[i]+1
        i = i+1


# from 3 to 9, first is 3,next will be 5 , 7
def listOfPrime(start,end):
    lst = []
    
    nxt = start
    if isPrimeNumber(start):
        nxt = start
    else:
        nxt = findNextPrime(start)

    #print(nxt, end=', ')
    lst.append(nxt)
    while nxt <= end:
        nxt = findNextPrime(nxt)
        #print(nxt, end=', ')
        if nxt<=end:
            lst.append(nxt)

        
    return lst
        

#List of something

def myProgram():

    keyword = ['def', 'while', 'if', 'elif', 'else', 'break', 'for', 'in']
    printAList(keyword)

#write a function that will give me sum of all prime number within a given range (a,b)  
def sumOfPrimeRange(start,end):
    primes=listOfPrime(start,end)
    result = sumOfList(primes)
    return result

def sumOfList(lst):
    i = 0
    sm = 0
    while i < len(lst):
        sm = sm+lst[i]
        i = i+1  
    return sm

#lst = [1,42,24,31,65]

def sumOfEven(lst):
    i = 0
    sm = 0
    while i < len(lst):
        if lst[i]% 2 == 0:
            sm = sm+lst[i]
        i = i+1  
    return sm

def sumOfOdd(lst):
    i = 0
    sm = 0
    while i < len(lst):
        if lst[i]% 2 == 1:
            sm = sm+lst[i]
        i = i+1  
    return sm
    
def printAList(lst):
    i = 0
    while i < len(lst):
        print(lst[i],end=',')
        i = i+1    
    
def averageOfNumbers(lst):
    a = sumOfList(lst)
    b = float(a)/ len(lst)
    return b
    
