# Data Structures library for Python

## Included Data Structures

1. Linked list
2. Stacks
3. Queues
4. Trees
5. Graphs
6. Heaps


# Linked List

- A doubly linked list

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
