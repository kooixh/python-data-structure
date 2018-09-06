#class to represent a node in a linked list
class Node():

    def __init__(self,value):
        self.val = value
        self.prev = None
        self.next = None

    def __eq__(self,obj):
        if isinstance(obj,Node):
            return self.val == obj.val

class LinkedList():

    #initialise an empty linked lsit
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isempty(self):
        return self.length == 0
    #add a new element to the linked list
    def add(self,val):
        node = Node(val)
        self.length+=1
        if(self.head == None):
            self.head = node
        elif (self.tail == None):
            self.head.next = node
            node.prev = self.head
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    #Remove the first occurance of val in the list
    def remove(self,val):
        if not self.isempty():
            h = self.head
            if(h != None and h.val == val):
                if(h == self.head):
                    h.next.prev = None
                    self.head= h.next
                elif(h == self.tail):
                    h.prev.next = None
                    self.tail = h.prev
                else:
                    h.prev.next = h.next
                    h.next.prev = h.prev
                self.length -=1
                return True
        return False


    #get the value at idx, raise Index Error or out of bounds exception
    def get(self, idx):
        if not self.isempty():
            h = self.head
            for i in range (0,idx):
                if(h==None):
                    break
                h = h.next
            if h != None:
                return h.val
        raise IndexError('Index out of range')



if __name__ == '__main__':
    ll = LinkedList()
