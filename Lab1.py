
#Task1--------------
print("Hello, World!")


#Task2--------------
x =1 
#the initial value of x is 1
if x>0:
    print("These are two comments") #Print a string


#Task3---------------
txt=input("Type something to test this out: ")
print(txt)


#Task4---------------
print("Statements1")
print("Statement2")
#you can write two statements in following way
print("Statements1");print("Statement2")


#Task5---------------
y=1
if y>0 :
 print ("This statement has no indentation")
 print ("This statement has no indentation")


#Task6----------------
z=1
if z>0 :
 print ("This statement has a single space indentation")
 print ("This statement has a single space indentation")
 

#Task7----------------
z=1
if z>0 :
    print ("This statement has space + tab indentation")
    print ("This statement has space + tab indentation")


#Task8----------------
a=1452
print(type(a))

b=(-4587)
print(type(b))

c=0
print(type(c))

g=1.03
print(type(g))

h=-11.23
print(type(h))

i=.34
print(type(i))

j=2.12e-10
print(type(j))

k=5E220
print(type(k))


#Task9----------------
x= complex(1,2)
type(x)
print(x)

z= 1+2j
type(z)
print(z)

z= 1+2J
type(z)
print(z)


#Task10------------------
x=True
type(x)
print(type(x))

y=False
type(y)
print(type(y))


#Task11------------------
str1="String1" #string start and end with double quotes
print(str1)

str2='String 2' #string start and end with double quotes
print(str2)

#str3='String"  #string start with single quote and end with double quotes #error
#print(str3)

#str4="String'  #string start with double quotes and end with single quotes
#print(str4)

str5="Day'sss" #single quote within double quotes
print(str5)

str2='Day"s ' #double quote within single quotes
print(str2)


#Task12-------------
print("This is a backslash (\\) mark.")

print("This is tab \t key")

print("These are \'single quotes\'")

print("These are \"double quotes\"  ")

print("This is a new line \nNew line")



#Task13-----------------
string1="PYTHON TUTORIAL"
print(string1[0])  #Print first Character

print(string1[-15])  #Print first Character

print(string1[14])  #Print last Character

print(string1[-1])  #Print last Character

print(string1[4])  #Print 5th Character

print(string1[-11])  #Print 5th Character

# print(string1[16])  #Print no Character(index do not exist)


#Task14-----------------
my_list1=[5,12,13,14] #the list contains all integer values
print(my_list1)

my_list2=['red','blue','black','white'] #the list contain ins all string values
print(my_list2)

my_list3=['red',12,112.2]   #the list contains string and integer and a float
print(my_list3)


#task15--------------
my_list=[]
print(my_list)


#task16----------------
color_list=["RED","BLUE","BLACK","WHITE"]   #The list have four elements indices start 0 and end at 3
color_list[0]  #Return  first Element
print(color_list[0],color_list[3]) #Return  first Element and last elements

color_list[-1] #return Last element
#print(color_list[4]) #This will raise an IndexError since the index is out of bounds


#task17-----------------
color_list=['Red','Blue','Black','White']  #The list have four elements indices start 0 and end at 3
print(color_list[0:2]) #cut first two items

print(color_list[1:2]) #cut second items

print(color_list[1:-2]) #cut second items

print(color_list[:3]) #cut first three  items

print(color_list[:]) #Creates copy of original line


--------------------------Algorithms of linear Search------------------------

#algo1--------------Find number in an array
arr=[10,20,30,40,50]
t=int(input("Enter number: "))
numfound=False
for i in range(len(arr)):
    if arr[i]==t:
        found=True
        break
if numfound:
    print("Number found..")
else:
    print("Number not found..")


#algo2------------------Find number in two arrays A and B
A=[10,20,30,40,50]
B=[5,2,0,3,4]

t=int(input("Enter number: "))
numfound = False

for i in range(len(A)):
    if A[i]==t:
        numfound=True
        break

if not numfound:
    for i in range(len(B)):
        if B[i]==t:
            numfound=True
            break

if numfound:
    print("Number found")
else:
    print("Number not found")


#algo3---------------------Find common number in two Arrays
A=[10,20,30,40,50]
B=[15,25,30,45,50]

numfound=False

for i in range(len(A)):
    for j in range(len(B)):
        if A[i]==B[j]:
            numfound=True
            break
if numfound: 
    print("Common number found")        
else:   
    print("Common number not found")


#algo4-----------------------Find duplicate number in An Array
A=[10,20,30,40,50]

for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[i]==A[j]:
            print("Duplicate number found...true")
            break
    else:
        continue
    break
else:
    print("Duplicate num not found...")
