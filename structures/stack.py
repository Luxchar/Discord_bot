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