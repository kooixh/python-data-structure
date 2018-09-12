class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedQueue():

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def isempty(self):
        return self.length == 0

    def offer(self,val):
        n = Node(val)
        #if queue is empty add to head
        if self.isempty():
            self.head = n
        elif self.tail == None: #if not empty but tail is none, only one element, add to tail
            self.tail = n
            self.head.next = self.tail
        else: #else add to the end
            self.tail.next = n
            self.tail = n
        self.length += 1
    #return and remove head element
    def poll(self):
        if(self.isempty()):
            raise IndexError('Queue is empty')
        else:
            self.length -=1
            val = self.head.val
            self.head = self.head.next
            if(self.isempty()):
                self.tail = None
            return val
