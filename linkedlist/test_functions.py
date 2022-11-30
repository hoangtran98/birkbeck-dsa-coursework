import unittest
from functions import *
from linkedlist import *


class test_functions(unittest.TestCase):
    def test_sumEvenList(self):
        inputData = [10, 20, 30, 40, 50]

        ll = LinkedList()
        ll.head = Node(inputData[0])
        temp = ll.head

        for i in range(1, len(inputData)):
            temp.next = Node(inputData[i])
            temp = temp.next

        self.assertEquals(sumEvenList(ll), 90)

    def testCase1_SecLargestList(self):
        # test case 1
        inputData = [10, 20, 30, 40, 50]

        ll = LinkedList()
        ll.head = Node(inputData[0])
        temp = ll.head

        for i in range(1, len(inputData)):
            temp.next = Node(inputData[i])
            temp = temp.next

        self.assertEqual(SecLargestList(ll), 40)

    def testCase2_SecLargestList(self):
        # test case 2
        inputData = [10]

        ll = LinkedList()
        ll.head = Node(inputData[0])
        temp = ll.head

        for i in range(1, len(inputData)):
            temp.next = Node(inputData[i])
            temp = temp.next

        self.assertEqual(SecLargestList(ll), -1)

    def testCase3_SecLargestList(self):
        # test case 3
        inputData = [10, 8]

        ll = LinkedList()
        ll.head = Node(inputData[0])
        temp = ll.head

        for i in range(1, len(inputData)):
            temp.next = Node(inputData[i])
            temp = temp.next

        self.assertEqual(SecLargestList(ll), 8)

    def testCase4_SecLargestList(self):
        # test case 4
        inputData = [8, 10]

        ll = LinkedList()
        ll.head = Node(inputData[0])
        temp = ll.head

        for i in range(1, len(inputData)):
            temp.next = Node(inputData[i])
            temp = temp.next

        self.assertEqual(SecLargestList(ll), 8)

    def testCase5_SecLargestList(self):
        # test case 5
        inputData = [1, 2, 3, 4, 5, 8, 6, 7]

        ll = LinkedList()
        ll.head = Node(inputData[0])
        temp = ll.head

        for i in range(1, len(inputData)):
            temp.next = Node(inputData[i])
            temp = temp.next

        self.assertEqual(SecLargestList(ll), 7)

    def test_reverseLinkedList(self):
        inputData = [1, 2, 8, 6, 7]

        ll = LinkedList()
        ll.head = Node(inputData[0])
        temp = ll.head

        for i in range(1, len(inputData)):
            temp.next = Node(inputData[i])
            temp = temp.next

        self.assertEqual(toList(reverseLinkedList(ll)), [7, 6, 8, 2, 1])

    def test_reverseLinkedListRec(self):
        inputData = [1, 2, 8, 6, 7]

        ll = LinkedList()
        ll.head = Node(inputData[0])
        temp = ll.head

        for i in range(1, len(inputData)):
            temp.next = Node(inputData[i])
            temp = temp.next

        self.assertEqual(toList(ReverseListRec(ll)), [7, 6, 8, 2, 1])
