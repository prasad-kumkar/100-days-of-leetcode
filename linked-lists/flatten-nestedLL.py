from LinkedList import *

l1 = LinkedList()
l1.append(5)
l1.append(9)

l2 = LinkedList()
l2.append(7)
l2.append(8)

def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    '''
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    '''
    res = LinkedList()
    print(list1.head.value)
    l1_node = list1.head
    l2_node = list2.head
    
    while list1 and list2:
        if l1_node.value < l2_node.value:
            res.append(l1_node.value)
            l1_node = l1_node.next
            
        elif l1_node.value > l2_node.value:
            res.append(l2_node.value)
            l2_node = l2_node.next
            
        else:
            res.append(l1_node.value)
            res.append(l2_node.value)
            l1_node = l1_node.next
            l2_node = l2_node.next
    return res

print(merge(l1,l2).to_list())

