#task1---------------
#python program to illustrate
#while loop
count=0
while (count<3):
    count=count+1
    print("Hello Geek")


#task2-----------------
#python program to illustrate
#single statement while block
'''count=0
while (count==0):print("Hello Geek")'''


#task3-------------------
#python program to illustrate
#iterating over a list
print("List iteration")
list=["geeks","for","geeks"]
for i in list:
    print(i)

#task4------------------
#iterating over a tuple (immutable)
print("\nTuple Iteration")
t=("geeks","for","geeks")
for i in t:
    print(i)

#task5------------------
#Iterating over a string
print("\nString Iteration")
s="Geeks"
for i in s:
    print(i)

#task6-------------------
#python program to illustrate
#iterating by index
list=["geeks","for","geeks"]
for index in range(len(list)):
    print(list[index])

#task7-------------------
#continue Statement
#print all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter=='e' or letter=='s':
        continue
    print('Current Letter:',letter)

#break statement
for letter in 'geeksforgeeks':
    #break the loop as soon it sees 'e' or 's'
    if letter=='e' or letter=='s':
        break
    print('Current Letter:',letter)


#task8------------------Functions
def my_function(): #creating a function
    print("Hello from a function")
my_function()   #function call


#task9--------------------Parameters
def my_function2(fname):
    print(fname+" Refsnes")
my_function2("Emil")
my_function2("Tobias")
my_function2("Linus")


#task10--------------------dafault parameter value
def my_function(country="Norway"):print("I am from "+country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#task10-------------passing a list as a parameter
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)


#task11----------------return values
def my_function2(x):
    return 5*x
print(my_function2(3))
print(my_function2(4))
print(my_function2(5))


#task12--------------------keyword arguments
def my_function3(child3,child2,child1):
    print("The youngest child is "+child3)

my_function3(child1= "Emil", child2="Tobias",child3="Linus")


#task13-----------------creating a class
class my_class:
    x=5
p1=my_class()
print(p1.x)

#task14------------------init_function
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("Emil",20)
print(p1.name)
print(p1.age)


#task15--------------------object methods
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def my_function(self):
        print("Hello my name is "+self.name)
p1=Person("Emil",20)
p1.my_function()
