import unittest
from arraystack import ArrayStack
from linkedstack import LinkedStack


class StackUnitTest(unittest.TestCase):

    def test_push(self):
        a = ArrayStack()
        l = LinkedStack()

        a.push(1)
        a.push(2)
        a.push(3)

        l.push(4)
        l.push(5)
        l.push(6)

        self.assertEqual(a.pop(),3)
        self.assertEqual(a.pop(),2)
        self.assertEqual(a.pop(),1)

        self.assertEqual(l.pop(),6)
        self.assertEqual(l.pop(),5)
        self.assertEqual(l.pop(),4)

        with self.assertRaises(IndexError):
            a.pop()
        with self.assertRaises(IndexError):
            l.pop()

    def test_peek(self):
        a = ArrayStack()
        l = LinkedStack()

        a.push(1)
        a.push(2)
        a.push(3)

        l.push(4)
        l.push(5)
        l.push(6)
        #test peek does not remove
        self.assertEqual(a.peek(),3)
        self.assertEqual(a.pop(),3)
        self.assertEqual(l.peek(),6)
        self.assertEqual(l.pop(),6)
        self.assertEqual(a.peek(),2)
        self.assertEqual(l.peek(),5)

if __name__ == '__main__':
    unittest.main()
