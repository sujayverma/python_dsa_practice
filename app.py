class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:      
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True


node = LinkedList(4)
# print(node.head)
# print(node.head.value)
# print(node.head.next)
# print(node.head.value)
# print(node.tail.next)

# node.append(5)
# node.prepend(3)
# print('\n')
# print(node.head.value)
# print(node.head.next.value)
# print(node.tail.value)
# print(node.tail.next)

print('\n')
# node.print_list()
print('\n')
print(node.pop().value)

print(node.pop())
