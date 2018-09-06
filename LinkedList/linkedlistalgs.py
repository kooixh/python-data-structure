from linkedlist import LinkedList

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


#split a linked list from l to r
def split(ll,l,r):
    a = LinkedList()

    if l>ll.length:
        raise IndexError('Index out of bounds')

    h = ll.head
    #head to lth element
    for i in range(l):
        h = h.next

    for i in range (r-l):
        a.add(h.val)
        h = h.next
    return a

#merge 2 sorted linked list head
def merge(a,b):
    if a == None:
        return b
    if b == None:
        return a

    if a.val<=b.val:
        temp = a
        temp.next = merge(a.next,b)
    else:
        temp = b
        temp.next = merge(a,b.next)
    return temp

def mergesort(n):
    #TODO implement

    '''
        n is none or n.next is None
            return None

        m = get middle
        n=mergesort(n)
        m=mergesort(m)

        merge(n,m)
    '''





if __name__ == '__main__':

    ll = LinkedList()

    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.add(6)
    ll.add(7)
    ll.add(8)

    reverse(ll)

    i = ll.iterator()

    while(i.hasnext()):
        print i.next()
