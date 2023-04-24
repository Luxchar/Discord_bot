from tree_node import Node
class Stack:
    def __init__(self, data):
        self.head = Node(data)
        
    def push(self, data): # add to the top of the stack
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def pop(self): # remove from the top of the stack
        if self.head is None:
            return None
        popped = self.head
        self.head = self.head.next
        return popped.data
    
    def size(self): # return the size of the stack
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def peek(self): # return the top of the stack
        if self.head is None:
            return None
        return self.head.data
    
    def print_index(self, index): # if index == 0, return the 10 at the top of the stack
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return None
    
    def clear(self):
        self.head = None

test = Stack(10)