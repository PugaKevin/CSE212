# QUEUE
We all had to experience the sadness of waiting in queue for anything, while sitting there have you wonder if there was a different process, or how queues work in other places? 

Like our cousing Stack, queue is a linear data structure that store items in First In First out. We will use the acronym FIFO because why not. The best way to explain it would be a deli meat where you would get a number and wait for your number to be called. If you get there first, then they will call your name first, hence, first in first out. FIFO. 

![Queue Example](Images/Queue.png)

## Terms to know
* Enqueue: "En" in latin means in or into. Using the Enqueue will add items to the queue. 
* Dequeue: Removes item from the queue. Think of the word decrease and what beginning part of it which is DE. If you decrease something you make it smaller. That what dequeue does. It remeoves from the queue. 

# Syntax

* Creating a queue
```
myQueue = list()
```
* Creating a enqueue function. The append fuction adds the element to the end of the list. 
```
def enqueue(myQueue, element):
    myQueue.append(element)
```
* Creating an isEmpty fuction, this is needed in order to undertand the dequeue.
```
def isEmpty(myQueue):
    if len(myQueue) == 0: 
        return True
    else: 
        return False
```

* Creating a dequeue function, or deleting an element from the front of the queue. The pop() function with the index of 0 will delete the element in the front. 
```
def  dequeue(myQueue):
    if not (isEmpty(myQueue)): 
        return myQueue.pop(0)
    else: 
        print("Queue is empty")
```

* Creating size function, returns the number of elements in your queue. 
```
def  size(myQueue):
    return len(myQueue)
```
* Creating a function to see what is at the front of the queue. You can call it anything you want. I will call it, WhatsInTheFront()
```
def  WhatsInTheFront(myQueue): 
    if isEmpty(myQueue): 
        print('Queue is empty')
        return None
    else: 
        return myQueue[0]
```

# Examples
```
myQueue = list()
# each person to be assigned a code as P1, P2, P3,...
element = input("enter person’s code to enter in queue :”)
enqueue(myQueue,element)

element = input("enter person’s code for insertion in queue:")
enqueue(myQueue,element)

print("person removed from queue is:", dequeue(myQueue))
print(“Number of people in the queue is :”,size(myQueue))

element = input("enter person’s code to enter in queue :")
enqueue(myQueue,element)

element = input("enter person’s code to enter in queue :")
enqueue(myQueue,element)

element = input("enter person’s code to enter in queue :")
enqueue(myQueue,element)

print("Now we are going to remove remaining people from the queue")

while not isEmpty(myQueue):
 print("person removed from queue is ",
 dequeue(myQueue))
```
OUTPUT:

enter person’s code to enter in queue :P1<br>
enter person’s code to enter in queue :P2<br>
person removed from the queue is :p1<br>
number of people in the queue is :1<br>
enter person’s code to enter in queue :P3<br>
enter person’s code to enter in queue :P4<br>
enter person’s code to enter in queue :P5<br>
Now we are going to remove remaining people from the queue<br>
person removed from the queue is :p2<br>
person removed from the queue is :p3<br>
person removed from the queue is :p4<br>
person removed from the queue is :p5<br>
Queue is empty


# Problem to Solve
Let us REVERSE IT! 

![Confused](Images/why.gif)




```
class Stack:
     def __init__(node):
         node.data = []
     def Empty(node):
         return node.data == []
     def push(node, data):
         node.data.append(data)
     def pop(node):
         return node.data.pop()
class Queue:
    def __init__(node):
        node.data = []
    def Empty(node):
        return node.data == []
    def enQueue(node, data):
        node.data.insert(0,data)
    def deQueue(node):
        return node.data.pop()
def Reverse():
    //Insert Code here to reverse it! 
    pass
    
S = Stack() 
Q = Queue()
Q.enQueue(5)
Q.enQueue(4)
Q.enQueue(3)
Q.enQueue(2)
Q.enQueue(1)
print(Q.data)
Reverse()
print(Q.data)
```
[Link to the solution](solution1.py)