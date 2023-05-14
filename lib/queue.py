class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue: # add data to the end of the queue, remove data from the front of the queue
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.size = 1
        
    def enqueue(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next
        self.size += 1
    
    def dequeue(self):
        head = self.head
        self.head = self.head.next
        self.size -= 1
        return head.data
        
    def peek(self): # return the first element in the queue which is the head
        return self.head.data
    
    def __len__(self):
        return self.size