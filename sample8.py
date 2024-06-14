class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def find_middle(self):
        if not self.head:
            print("List is empty")
            return None
        
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        
if __name__ == "__main__":
    sll = SingleLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.print_list()  
    print("Middle element:", sll.find_middle())

    sll2 = SingleLinkedList()
    sll2.append(1)
    sll2.append(2)
    sll2.append(3)
    sll2.append(4)
    sll2.append(5)
    sll2.append(6)
    sll2.print_list() 
    print("Middle element:", sll2.find_middle())
