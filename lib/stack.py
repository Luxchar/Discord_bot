class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack: # add data to the top of the stack, remove data from the top of the stack
    def __init__(self, data):
        self.head = Node(data)
        self.index = 0
        self.size = 1
        
    def push(self, data): # add to the top of the stack
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def pop(self): # remove from the top of the stack
        if self.head is None:
            return None
        popped = self.head
        self.head = self.head.next
        self.size -= 1
        return popped.data
    
    def peek(self): # return the top of the stack
        if self.head is None:
            return None
        return self.head.data
    
    # def print_index(self, index): # if index == 0, return the 10 at the top of the stack
    #     current = self.head
    #     count = 0
    #     while current:
    #         if count == index:
    #             return current.data
    #         count += 1
    #         current = current.next
    #     return None
    
    def print_index(self, index): # return the index-th element of the stack
        current = self.head
        count = 1
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return "Index out of range"
    
    def clear(self):
        self.head = None
        self.size = 0
        self.index = 0
        
    def get_size(self):
        return self.size
    
    def get_index(self):
        return self.index
    
    def increment_index(self):
        self.index += 1
        
    def decrement_index(self):
        self.index -= 1