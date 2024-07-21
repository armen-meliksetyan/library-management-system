class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def remove_last(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        current = self.head
        while current.next != self.tail:
            current = current.next
        current.next = None
        self.tail = current
    
    def print(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
            