
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('None')

    def delete(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            return
        
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            print("Node with data '{data}' not found")
            return
        
        prev_node.next = current_node.next

ll = LinkedList()
ll.append("Edmar")
ll.append("Queena")
ll.append("Luigi")
ll.append("Gerlie")
ll.append("Markvin")

print("Linked list after appending names:")
ll.display()

ll.delete("Gerlie")
print("\n""Linked list after deleting 'Gerlie':")
ll.display()
