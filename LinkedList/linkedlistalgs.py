from linkedlist import LinkedList
from linkedlist import Node

#reversing a linked list
def reverse(ll):
    t = ll.head
    ll.head = ll.tail
    ll.tail = ll.head
    cur = t

    while(cur != None):
        next = cur.next #next node to swap
        #swap prev and next
        cur.next = cur.prev
        cur.prev = next
        cur = next

#get the middle node of a linked list
def getmiddle(h):

    if h == None:
        return h
    i = h #slow
    j = h #fast


    while j.next != None and j.next.next !=None:
        i = i.next
        j = j.next.next

    return i


#merge 2 sorted linked list head
def merge(a,b):
    temp = None
    if a == None:
        return b
    if b == None:
        return a

    if a.val<=b.val:
        temp = a
        temp.next = merge(a.next,b)
        temp.next.prev = temp
        temp.prev =None
    else:
        temp = b
        temp.next = merge(a,b.next)
        temp.next.prev = temp
        temp.prev=None
    return temp

#merget sort a linked list given the head element
def mergesort(n):
    if n == None or n.next == None:
        return n

    m = getmiddle(n)
    r = m.next
    m.next = None

    n = mergesort(n)
    r = mergesort(r)

    return merge(n,r)


if __name__ == '__main__':

    ll = LinkedList()

    ll.add(10)
    ll.add(42)
    ll.add(3)
    ll.add(48)
    ll.add(15)
    ll.add(26)
    ll.add(71)
    ll.add(8)
    ll.add(34)


    ll.head = mergesort(ll.head)

    i = ll.iterator()

    while(i.hasnext()):
        print i.next()
