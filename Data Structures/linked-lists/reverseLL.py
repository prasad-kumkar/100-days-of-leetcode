from LinkedList import *

def reverse(linked_list):
    res = LinkedList()
    for value in iter(linked_list):
        res.append(value)
        
    return res

l = LinkedList()
l.append(5)
l.append(3)
l.append(1)
l.append(4)
flipped = reverse(l)
print(l.to_list(), flipped.to_list())