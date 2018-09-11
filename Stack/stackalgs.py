from linkedstack import LinkedStack

#reverse the stack given the top node
def reverse(p,n):
    #if is the bottom of the stack
    if n.next == None:
        n.next = p
        return n
    else:
        last= reverse(n,n.next)
        n.next = p
        return last

def reverseStack(ls):

    ls.top = reverse(None,ls.top)
    return ls



if __name__ == '__main__':
    l = LinkedStack()

    l.push(6)
    l.push(5)
    l.push(4)
    l.push(3)
    l.push(2)
    l.push(1)

    reverseStack(l)

    while(not l.isempty()):
        print l.pop()
