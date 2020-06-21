class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = self.head
    

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            return
        node = Node(value)
        node.next = self.head
        self.head = node
        return
    
    
    def append(self, value):
        """ Append a value to the end of the list. """    
        
        if self.head == None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
            
        node.next = Node(value)
        return
    
    
    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        return "Not found"
    
    
    def remove(self, value):
        """Remove first occurance of node with given value"""
        
        node = self.head
        if node.value == value:
            self.head = node.next
            return
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next
        
        return "Not found"
    
    
    def pop(self):
        """ Return the first node's value and remove it from the list. """
        
        value = self.head.value
        self.head = self.head.next
        return value
    
    
    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        # If the list is empty 
        if self.head is None:
            self.head = Node(value)
            return

        if pos == 0:
            self.prepend(value)
            return

        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return

            index += 1
            node = node.next
        else:
            self.append(value)
        
    
    def size(self):
        """ Return the size or length of the linked list. """
        if self.head ==0:
            return 0
        node = self.head
        size = 1
        while node:
            size+=1
            node = node.next
        return size

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out