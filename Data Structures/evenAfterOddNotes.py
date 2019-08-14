# Given a linked list with integer data, arrange the elements in such a manner 
# that all nodes with even numbers are placed after odd numbers. Do not create 
# any new nodes and avoid using any other data structure. The relative order of 
# even and odd elements must not change.
#
# Example:
# linked list = 1 2 3 4 5 6
# output = 1 3 5 2 4 6

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    currentHead = head
    currentNode = head
    prevNode = head
    curValue = 0
    prevValue = 0
    
    print("BEFORE LOOP: Current Head Value: {}; Current Node Value: {}; Prev Node Value: {}".format(currentHead.data, currentNode.data, prevNode.data))

    while currentHead.next != None:
        if currentNode.data % 2 == 1:                           # If Current Node value is odd
            if currentNode == currentHead:                      # AND, if Current Node is the HEAD
                currentNode = currentNode.next
                currentHead = currentNode
            else:                                               # If "odd" Current Node is not the HEAD
                if prevNode.data % 2 == 1:                      # is previous node an odd one too? If yes, continue
                    continue
                else:                                           # else swap value with it, to move odd left, even right
                    tempValue = prevNode.data
                    prevNode.data = currentNode.data
                    currentNode.data = tempValue
                print(prevNode == head)
        break
    
    print("AFTER LOOP: Current Head Value: {}; Current Node Value: {}; Prev Node Value: {}".format(currentHead.data, currentNode.data, prevNode.data))

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]
    
    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)    
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")            
    except Exception as e:
        print("Fail")

arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)