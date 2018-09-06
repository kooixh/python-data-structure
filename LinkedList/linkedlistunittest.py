import unittest
from linkedlist import LinkedList

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
            
if __name__ == '__main__':
    unittest.main()
