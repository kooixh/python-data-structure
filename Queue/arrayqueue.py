class ArrayQueue():
    """docstring for ArrayQueue."""
    def __init__(self):
        self.array = []
    #check if the queue is empty
    def isempty(self):
        return len(self.array) == 0
    #add to the queue
    def offer(self,val):
        self.array.append(val)
    #get and remove the head of the queue
    def poll(self):
        return self.array.pop(0)
    #get and do not remvoe head of queue
    def peek(self):
        return self.array[0]    
