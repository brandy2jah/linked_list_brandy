class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index")
            return
        if index == 0:
            self.insert_at_start(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1
        if not current:
            print("Index out of bounds")
            return
        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, index):
        if index < 0 or not self.head:
            print("Invalid index or empty list")
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current.next and count < index - 1:
            current = current.next
            count += 1
        if not current.next:
            print("Index out of bounds")
            return
        current.next = current.next.next

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def display(self):
        current = self.head
        if not current:
            print("Empty list")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



