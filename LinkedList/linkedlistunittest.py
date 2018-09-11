import unittest
from linkedlist import LinkedList
from linkedlistalgs import mergesort

#unit tests to test all the implementation of the linked list
class TestLinkedList(unittest.TestCase):

    #Test adding new element and next points to correct element
    def test_add(self):
        l = LinkedList()
        l.add(1)
        l.add(2)
        l.add(3)
        l.add(4)
        h = l.head
        self.assertEqual(h.val,1)
        h=h.next
        self.assertEqual(h.val,2)
        h = h.next
        self.assertEqual(h.val,3)
        h=h.next
        self.assertEqual(h.val,4)

    #test previous points to correct element
    def test_prev(self):
        l = LinkedList()
        l.add(1)
        l.add(2)
        l.add(3)
        l.add(4)
        h = l.tail
        self.assertEqual(h.val,4)
        h=h.prev
        self.assertEqual(h.val,3)
        h = h.prev
        self.assertEqual(h.val,2)
        print h.next.val
        h=h.prev
        self.assertEqual(h.val,1)

    def test_get(self):
        l = LinkedList()
        l.add(1)
        l.add(2)
        l.add(3)
        l.add(4)

        self.assertEqual(l.get(0),1)
        self.assertEqual(l.get(3),4)
        with self.assertRaises(IndexError):
            l.get(6)

    def test_remove(self):
        l = LinkedList()
        l.add(1)
        l.add(2)
        l.add(3)
        l.add(4)

        l.remove(1)

        self.assertEqual(l.get(0),2)

    def test_clear(self):
        l = LinkedList()
        l.add(1)
        l.add(2)
        l.add(3)
        l.add(4)

        l.clear()
        self.assertEqual(l.head,None)
        self.assertEqual(l.tail,None)
        self.assertEqual(l.length,0)

    def test_contains(self):
        l = LinkedList()
        l.add(1)
        l.add(2)
        l.add(3)
        l.add(4)

        self.assertEqual(l.contains(1),True)
        self.assertEqual(l.contains(8),False)

    def test_iterator(self):
        l = LinkedList()
        l.add(1)
        l.add(2)
        l.add(3)
        l.add(4)

        i = l.iterator()
        v = 1
        while i.hasnext():
            self.assertEqual(i.next(),v)
            v+=1
    def test_toarray(self):
        l = LinkedList()
        l.add(1)
        l.add(2)
        l.add(3)
        l.add(4)

        self.assertEqual([1,2,3,4],l.toarray())

    def test_sort(self):
        l = LinkedList()
        l.add(28)
        l.add(7)
        l.add(13)
        l.add(4)

        l.head = mergesort(l.head)
        n = l.head.next
        lastval = l.head.val

        #the next value is always greater than the last
        while(n != None):
            self.assertEqual(n.val>=lastval,True)
            lastval = n.val
            n = n.next


if __name__ == '__main__':
    unittest.main()
