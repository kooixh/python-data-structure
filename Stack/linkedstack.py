class Node():
    def __init__(self,val):
        self.val = val
        self.next = None


class LinkedStack():
    """Implementation of a stack using linked list."""
    def __init__(self):
        self.top = None
        self.size = 0

    #check if stack is empty
    def isempty(self):
        return self.size == 0

    def push(self,val):
        self.size += 1
        if(self.isempty()):
            n = Node(val)
            self.top = n
        else:
            n = Node(val)
            n.next = self.top
            self.top = n

    #return the top element and remove the item
    def pop(self):
        if(self.isempty()):
            raise IndexError('Stack is empty')
        else:
            n = self.top
            self.top = self.top.next

            self.size -= 1
            return n.val
    #get the top element without removing the item
    def peek(self):
        if(self.isempty()):
            raise IndexError('Stack is empty')
        else:
            return self.top.val
