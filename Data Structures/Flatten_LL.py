############ Flattening a nested linked list ############
# Suppose you have a linked list where the value of each node is a sorted linked list 
# (i.e., it is a nested list). Your task is to flatten this nested list—that is, to 
# combine all nested lists into a single (sorted) linked list.

# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self, head):
        self.head = head
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

def merge(list1, list2):
    """
    Merge and sort two linked lists

    Args:
       list1, list2: two linked lists that need to be merged. They need to be pre-sorted before being passed as a argument.
    Returns:
       linked-list: Merged and sorted linked-list, a combination of list1 and list2
    """
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged

class NestedLinkedList(LinkedList):
    def flatten(self):
        # TODO: Implement this method to flatten the linked list in ascending sorted order.
        pass

# First Test scenario
linked_list = LinkedList(Node(1))
linked_list.append(Node(3))
linked_list.append(Node(5))

# nested_linked_list = NestedLinkedList(Node(linked_list))

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

merged = merge(linked_list, second_linked_list)
node = merged.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next
    
# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next
# nested_linked_list.append(Node(second_linked_list))