# Data Structures library for Python

## Included Data Structures

1. Linked list
2. Stacks
3. Queues
4. Trees
5. Graphs
6. Heaps


# Linked List

A doubly linked list

## Usage
- Creating and adding to linked list
```python
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
```
Linked list created will be

1->2->3->4

1<-2<-3-<4

- Getting value from linked list

```python
l.get(1)
```
Value returned is the one at index 1(second element) which is 2

- Removing an element

```python
l.remove(3)
```

First occurrence of 3 will be removed.

Linked list is now

1->2->4

1<-2<-4

- Iterating over linked list

```python
itr = l.iterator()

while(itr.hasnext()):
  print itr.next()
```
`l.iterator()` returns a new iterator from the head

`itr.hasnext()` checks if there is a next element

`itr.next()` get's the value at the index and go to the next index

# Stacks

A Last In First Out(LIFO) Data Structure implemented using arrays and linked list

## Usage

`push(e)` adds an element to the top of the stack

`pop()` retrieves and removes the top element

`peek()`retrieves and does not remove the top element


```python
a = ArrayStruct() #create an array struct
l = LinkedStruct() #create a linked struct

a.push(1) #add the element 1 to the top of the Stack
a.push(2) #add 2 to the top of stack
a.push(3) #add 3

print a.pop() #prints 3
print a.peek() #prints 2
print a.pop() #prints 2
print a.pop() #prints 1

#same for linked stack
l.push(4) #add 4
l.push(5) #add 5
l.push(6) #add 6

print l.pop() #prints 6
print l.pop() #prints 5
print l.peek() #prints 4
print l.pop() #prints 4
```


# Queue

A First in First out(FIFO) data structure implemented using arrays and linked list


## Usage

`offer(e)` adds a new element to the back of the queue

`poll()` retrieves and removes the front element

`peek()` retrieves and does not remove the front element

```python

a = ArrayQueue()
a.offer(1)
a.offer(2)
a.offer(3)

print a.poll() #prints 1
print a.poll() #prints 2
print a.peek() #prints 3
print a.poll() #prints 3

#same for linked stack
```
