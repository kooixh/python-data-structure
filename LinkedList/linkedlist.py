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
    #clear link list
    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0
    #check if a value is in a link list
    def contains(self,val):
        h = self.head
        while(h != None):
            if(h.val == val):
                return True
            h = h.next
        return False

    #add a new element to the linked list
    def add(self,val):
        node = Node(val)
        self.length+=1
        #if list is empty add as head
        if(self.head == None):
            self.head = node
        elif (self.tail == None): #if tail is empty while head is not, i.e second element
            self.head.next = node
            node.prev = self.head
            self.tail = node
        else:#otherwise add to the end of the list
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    #Remove the first occurance of val in the list
    def remove(self,val):
        if not self.isempty():
            h = self.head
            if(h != None and h.val == val):
                # if have to delete head, set head next's prev to None and set it to be head
                if(h == self.head):
                    h.next.prev = None
                    self.head= h.next
                elif(h == self.tail): # if have to delete tail, same concept as head
                    h.prev.next = None
                    self.tail = h.prev
                else: # otherwise point prev and next to each other
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
                    break # reach end of list
                h = h.next
            if h != None:
                return h.val
        raise IndexError('Index out of range')

    #get a new iterator for the linked list starting at the head
    def iterator(self):
        return LinkedListIterator(self.head)

    def toarray(self):
        h = self.head
        a= []
        while(h!=None):
            a.append(h.val)
            h=h.next
        return a


#linked list iterator class
class LinkedListIterator():
    #node to start iterating
    def __init__(self,node):
        self.node = node

    #return value and set node to be next node
    def next(self):
        if self.node == None:
            raise IndexError('Index out of range')
        v = self.node.val
        self.node = self.node.next
        return v
    #if there is more node to iterate over
    def hasnext(self):
        return self.node != None



if __name__ == '__main__':
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    itr = ll.iterator()

    while(itr.hasnext()):
        print itr.next()
