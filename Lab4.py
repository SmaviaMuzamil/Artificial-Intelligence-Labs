
#task1
#stack implementation
'''class Stack:

    def __init__(self):
        self.stack=[]

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty")
        else:
            value=self.stack[-1]
            self.stack.pop()
            print("Removed element:",value)

    def top(self):
        if len(self.stack)==0:
            print("Stack is empty")
            return None
        else:
            top=self.stack[-1]
            print("Top Element is: ",top)

    def display(self):
        print("Stack:",self.stack)
        print("Reversed Stack:",self.stack[::-1])


# Create object
s=Stack()

# Take input from user
n=int(input("Enter number of elements: "))

for i in range(n):
    value=int(input("Enter element: "))
    s.push(value)

s.display()

# Push
value=int(input("Enter element to push: "))
s.push(value)
s.display()
# P/op
s.pop()
s.top()
s.display()'''


#task2
#queue implementation
'''class Queue:

    def __init__(self):
        self.queue=[]

    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if len(self.queue)==0:
            print("Queue is empty")
        else:
            value=self.queue[0]
            for i in range(len(self.queue)-1):
                self.queue[i]=self.queue[i+1]
            self.queue.pop()
            print("Removed element:",value)
            
    def display(self):
        print("Queue:",self.queue)

# Create object
q=Queue()

# Take input from user
n=int(input("Enter number of elements: "))

for i in range(n):
    value=int(input("Enter element: "))
    q.enqueue(value)

q.display()

# Enqueue
value=int(input("Enter element to insert: "))
q.enqueue(value)

q.display()

# Dequeue
q.dequeue()

q.display()'''



#task3
#binary search...
# Binary Search
arr = [80, 28, 30, 0, 58, 26, 70, 80, 10]
arr.sort()
print(arr)
target=int(input("Enter value to search: "))
low=0
high=len(arr)-1
found=False
while low<=high:
    mid=(low+high)//2
    print("Middle element:",arr[mid])
    if arr[mid]==target:
        print("Element found at index:",mid)
        found=True
        break
    elif target<arr[mid]:
        high=mid-1
    else:
        low=mid+1
if found==False:
    print("Element not found")
