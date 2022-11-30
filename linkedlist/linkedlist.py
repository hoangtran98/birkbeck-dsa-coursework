class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None

class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def printLinkedList(self):

        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    linkedList = LinkedList()

    linkedList.head = Node(10)
    linkedList.head.next = Node(20)
    linkedList.head.next.next = Node(30)

    linkedList.printLinkedList()
