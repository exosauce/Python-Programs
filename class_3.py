def sumOfTwoDigits(x):
    first=x//100
    last=x%100
    return first+last


def largestNumber(a,b,c):
    if a>=b and a>=c:
        return a
    if b>=a and b>=c:
        return b
    if c>=a and c>=b:
        return c


def largestNumber2(a,b,c):
    large = c
    if a>=b and a>=c:
        large = a
    if b>=a and b>=c:
        large = b
    if c>=a and c>=b:
        large = c

    return large


def largestNumber3(a,b,c):
    large = c
    if a>=b and a>=c:
        large = a
    elif b>=c and b>= a:
        large = b
    else:
        large = c

    return large


def uniqueNumbers(a,b,c):
    if a==b or a==c:
        return False
    elif b==c:
        return False
    else:
        return True

#SumOfN(n) = 1+2+...+n

def doSomething(n):
    x = 0
    while n>0:
        x = x + n
        n = n-1

    return x

def factorial(n):
    x = 1
    while n>0:
        x = x*n
        n = n-1

    return x

# 567  => 765
# 7  56
# 6  5
# 5  0

def reverseNumber(n):
    x=0
    while n>0:
        d=n%10
        n=n//10
        x = d + x*10

    return x
# if n%2 == 0 that is even
def sumOfOdd(n):
    x = 0
    while n>0:
        if n%2 == 1:
            x = x + n
        n = n-1

    return x
    
