class ArrayStack():

    """Implementation of a stack using arrays"""
    def __init__(self):
        self.array = []
    #check if the array is empty
    def isempty(self):
        return len(self.array) == 0

    #add an element onto the stack
    def push(self,val):
        self.array.append(val)

    #get the element on top of the stack
    def pop(self):
        if(self.isempty()):
            raise IndexError('Stack is empty')
        else:
            return self.array.pop()
    #get the top element without Removing
    def peek(self):
        if(self.isempty()):
            raise IndexError('Stack is empty')
        else:
            return self.array[len(self.array)-1]
