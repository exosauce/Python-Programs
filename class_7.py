#Given two list, first list contains name of people and second list
#contains what those people like to eat.  Write a function that will answer what John like to eat.
# n1 = ['john', 'Chron', 'Zeron']
# f1 = ['Apple', 'Orange', 'Orange']


def nameEat2 (names, food, name):
    i = 0
    for abc in names:
        if(name == abc):
            return food[i]
        i = i+1
    
    return ""



def nameEat (names, food, name):
    i = 0
    for each in names:
        if(name == each):
            return food[i]
        i = i+1
    
    return ""


def nameFruit (names, food, name):
    i = 0
    for each in names:
        if(name == each):
            return food[i][0]
        i = i+1
    
    return ""
# n1 = ['john', 'Chron', 'Zeron']
# [0, 1, 2]
# f1 = ['Apple', 'Orange', 'Orange']
def nameFood  (names, food, name):
    
    for each in range(3): # x is going from 0 to len-1  len(names)
        if name == names[each]:
            return food[each]
        
    return None

def nameFoodTest  (names, food, name):
    
    for each in range(0,10,2): # x is going from 0 to len-1  len(names)
        print("My each is : " + str(each))
        
    return None



def nameFoodWhile (names, food, name):
    each = 0
    while each < len(names):  #logical expression / conditional statement
        if name == names[each]:
            return food[each]
        each = each+1
        
    return ""

'''
convert a decimal number into binary
        12%2  = 0
12//2 = 6
        6%2 = 0
6//2 = 3
        3%2 = 1
3//2 = 1
        1%2 = 1
1//2 = 0

1100


'''
def decToBin(dec):
    result = ''
    while dec > 0 :
        result = str(dec%2) + result
        dec = dec//2

    return result


'''
Factorial:
5! = 1*2*3*4*5 = 120
'''


def factorial (x):
    n=1
    while x>0:
        n = n*x
        x = x-1

    return n


def factorialForLoop (x):
    n=1
    for i in range(1,x+1):  
        n=n*i

    return n


'''
names = ['John', 'Chron', 'Tron']
passwords ['abcd', 'efgh', 'nmop']
'''

def userPassword():
    names = ['John', 'Chron', 'Tron']
    passwords =['abcd', 'efgh', 'nmop']
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    
    i = 0
    for each in names:
        if(name == each):
            if passwords[i] == password:
                print("Your password matched")
                return
        i = i+1
    print("Name or password is wrong!!!!!")


temparatures = [15, 12, 23, 31, 13, 34, 8, 2, -3, 4, 24, 28, 31, 32]

def highestTemp(lst):
    n=lst[0]
    for i in lst:
        if i > n:
            n=i

    return n

def lowestTemp(lst):
    n=lst[0]
    for i in lst:
        if i < n:
             n=i

    return n

    

''' Temperatures above 25 deg
returns a list days that are outdoor temperature'''
def outDoorTemp(lst):
    newLst = []
    for item in lst:
        if item > 25:
            newLst.append(item)

    return newLst

    
            
temparatures = [15, 12, 23, 31, 13, 34, 8, 2, -3, 4, 24, 28, 31, 32]
temparatures2 = [16, 12, 25, 18, 32, 35, 6, 8, -3, 4, 26, 28, 32, 32]

def tomorrowTemp(lst, lst2):
    newLst=[]
    for i in range(len(lst)):
        x = lst2[i]-lst[i]
        newLst.append(lst2[i]+x)
    return newLst
 


def highestTemp2 (lst, lst2):
    x = highestTemp(lst)
    y = highestTemp(lst2)

    return (x,y)

x = {"name":"John", "food":"Apple", "age": 32}
y = {"name":"Chron", "food":"Orange", "age": 64}
z = {"name":"Zohn", "food":"Grape", "age": 44}


people = [x,y,z]

def whoLikes(food, lst):
    for person in lst:
        if food == person['food']:
            return person['name']
    return None

whoLikes("Orange", people)


def oldestPerson(lst):
    age=0
    oldest = None
    for person in lst:
        if age < person['age']:
            age=person['age']
            oldest = person
            
    return oldest
            
'''
Name: Chron
Food: Orange
Age: 64
'''
course1={"name": "Math", "code":"MPM2DR", "grade":70}
course2={"name": "English", "code":"ENG2DR", "grade":85}
course3={"name": "Science", "code":"SNC2DR", "grade":92}	
course4={"name": "History", "code":"CHC2DR", "grade":74}
course5={"name": "French", "code":"FNC2DR", "grade":82}

person1 = {"name":"John", "age":21, "height":163, "weight":71}
person2 = {"name":"Jack", "age":18, "height":167, "weight":76}
person3 = {"name":"Jill", "age":20, "height":157, "weight":64}

student1 = {"person":person1, "studentNumber":123, "program":"computerScience", "GPA":0, "year": 2022, "courses":[]}
student2 = {"person":person2, "studentNumber":456, "program":"computerScience", "GPA":0, "year": 2022, "courses":[]}
student3 = {"person":person3, "studentNumber":789, "program":"computerScience", "GPA":0, "year": 2022, "courses":[]}


student1["courses"].append(course2)
student1["courses"].append(course4)
student1["courses"].append(course3)

student2["courses"].append(course1)
student2["courses"].append(course5)
student2["courses"].append(course3)


students = [student1, student2, student3]

def computeGPA(students):
    for student in students:
        courses = student["courses"]
        x=0
        for course in courses:
            x = x + course["grade"]
        if len(courses)>0:    
            student["GPA"]= x/len(courses)
        
            
def printGPA(students):
    for student in students:
        print(student["person"]["name"] + " GPA: " + str(student["GPA"]))
    


    
    
