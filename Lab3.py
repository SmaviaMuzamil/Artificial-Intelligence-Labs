#print the numbers btw 1500 and 2700 that is divisible by 7 and 5
#task1
'''for i in range(1500,2700):
    if i%7==0 and i%5==0:
        print(i)'''

'''#task2
#covert to and from Celcius  and Fahrenheit
temp=float(input("Enter temprature: "))
unit=input("Enter unit for temp C or F: ")
if(unit=="C"):
    f=(temp*9/5)+32
    print(temp,"C is",f,"in Farenheit")
elif(unit=="F"):
    c=(temp-32)*5/9
    print(temp,"F is",c,"in Farenheit")
else:
    print("Invalid unit")'''

'''#task3
#Guess a number between 1 and 9
import random
number=random.randint(1, 9)
while True:
    guess=int(input("Guess a number between 1 and 9: "))

    if (guess==number):
        print("Well guessed!")
        break
    else:
        print("Wrong guess, try again.")'''

#task4
#Two opposite right-angle triangles together
'''for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

for i in range(4,0,-1): 
    for j in range(i):
        print("*", end="")
    print()'''


#task5
#Reverse a word
'''word=input("Enter a word: ")
reverse=""
for i in range(len(word)-1,-1,-1):
   reverse+=word[i]
print("Reversed word:",reverse)'''


#task6
#count even and odd numbers
'''numbers=(1,2,3,4,5,6,7,8,9)
even=0
odd=0
for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd +=1
print("Number of even numbers:",even)
print("Number of odd numbers:",odd)'''


#task7
#print each item of list and its type
'''datalist=[1452,11.23,1+2j,True,'w3resource',(0,-1),[5,12]]
for item in datalist:
    print(item,type(item))'''


#task8
#print numbers 0 to 6 except 3 and 6
'''for num in range(7):
    if (num==3 or num==6):
        continue
    print(num)'''


#task9(a)
#Fibonacci Series btw 0 and 50
'''a=0
b=1
while a<=50:
    print(a,end=" ")
    c=a+b
    a=b
    b=c

#task9(b)
#fizzbuzz
for num in range(1,51):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)'''


#task10
#Two dimensional Array
'''rows=int(input("Enter number of rows: "))
columns=int(input("Enter number of columns: "))
array=[]
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(i * j)
    array.append(row)
print(array)'''


#task11
#Input lines until blank line, then print lowercase
'''lines=[]
while True:
    line=input()
    if line=="":
        break
    lines.append(line)
for line in lines:
    print(line.lower())'''


#task12
#4-digit binary numbers divisible by 5
'''numbers=input("Enter 4-digit binary numbers separated by commas: ")
numbers=numbers.split(",")
result=[]
for num in numbers:
    decimal=int(num,2)
    if decimal%5==0:
        result.append(num)
print(",".join(result))'''


'''#task13
#Count letters and digits
text=input("Enter a string: ")
letters=0
digits=0
for char in text:
    if char.isalpha():
        letters+=1
    elif char.isdigit():
        digits+=1
print("Letters",letters)
print("Digits",digits)'''


#task14
#Password validation
password = input("Enter your password: ")

lower=False
upper=False
digit=False
special=False
for char in password:
    if char.islower():
        lower=True
    elif char.isupper():
        upper=True
    elif char.isdigit():
        digit=True
    else:
        special=True
if len(password)<6 or len(password)>16:
    print("Invalid password: Length must be between 6 and 16 characters.")
elif not lower:
    print("Invalid password: At least one lowercase letter is required.")
elif not upper:
    print("Invalid password: At least one uppercase letter is required.")
elif not digit:
    print("Invalid password: At least one number is required.")
elif not special:
    print("Invalid password: At least one special character is required.")
else:
    print("Valid password")