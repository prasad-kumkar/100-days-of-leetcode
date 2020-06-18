from LinkedList import *

def reverse(linked_list):
    '''temp_list = []
    for value in iter(linked_list):
        temp_list.append(value)
    '''
    temp_list = linked_list.to_list()
    node = linked_list.head
    i=0
    while node:
        node.value = temp_list[i]
        i+=1
        print(node.value)
        node = node.next
    return linked_list

l = LinkedList()
l.append(5)
l.append(3)
l.append(1)
l.append(4)
flipped = reverse(l)
print(l.to_list(), flipped.to_list())