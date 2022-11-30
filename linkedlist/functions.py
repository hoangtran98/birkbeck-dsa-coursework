from linkedlist import LinkedList, Node

# Write a function SumEvenList whose input is a linked list and the output
# is the sum of even elements of the list.
def sumEvenList(l: LinkedList) -> int:

    i = 0
    sum = 0
    temp = l.head

    while temp:
        if i % 2 == 0:
            sum += temp.data
        temp = temp.next
        i += 1

    return sum


# Write a function SecLargestList whose input is a linked list. The function
# should return the second largest element of the list. If the list does not
# have the second largest element because the list contains less than two
# elements, the function should return -1.
def SecLargestList(l: LinkedList) -> int:
    maxEl = -1
    secEl = -1

    temp = l.head

    while temp:
        if not maxEl:
            maxEl = temp.data
            continue

        if temp.data > maxEl:
            secEl = maxEl
            maxEl = temp.data
        elif not secEl or maxEl >= temp.data > secEl:
            secEl = temp.data

        temp = temp.next

    return secEl


# Write a function ReverseListIter whose input is a linked list. The function
# should return a linked list with the same element but in the reverse order.
# For example, if the input list is 5 → 4 → 3 → 2 → 1 then the output list is
# 1 → 2 → 3 → 4 → 5. The function should use loops only (no recursion).


def reverseLinkedList(ll: LinkedList) -> LinkedList:

    prev = None
    cur = ll.head
    next = cur.next

    while cur:
        cur.next = prev

        prev = cur
        cur = next

        if next is not None:
            next = next.next

    ll.head = prev

    return ll


# Helper function: to convert a linked list to list
def toList(ll: LinkedList) -> list:

    res = []
    temp = ll.head

    while temp:
        res.append(temp.data)
        temp = temp.next

    return res


# Write a function ReverseListRec with the same input and output as ReverseListIter
# but this time, use recursion only and no loops.
def reverseLinkedListRec(node: Node, prev, head=None) -> Node:

    if node is None:
        return prev

    head = reverseLinkedListRec(node.next, node)
    node.next = prev

    return head


def ReverseListRec(ll: LinkedList) -> LinkedList:

    ll.head = reverseLinkedListRec(ll.head, None)

    return ll
