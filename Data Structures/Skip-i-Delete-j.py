# You are given the head of a linked list and two integers, i and j. 
# You have to retain the first i nodes and then delete the next j nodes. 
# Continue doing so until the end of the linked list.

# Example:
# linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
# i = 2
# j = 3
# Output = 1 2 6 7 11 12

# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    newHead = Node(head.data)
    newListNode = newHead
    currentNode = head
    # newListNode.next = Node(currentNode.next.data)
    # print_linked_list(newHead)
    retainCounter = 0
    deleteCounter = 0
    counter = 0
    
    # retainCounter -= 1
    # currentNode = currentNode.next
    print("BEFORE WHILE LOOP: Retain Counter: {}; Delete Counter: {}; Current Node: {}".format(retainCounter, deleteCounter, currentNode.data))
    print("BEFORE WHILE LOOP: NEW LINKED LIST")
    print_linked_list(newHead)
    while currentNode.next:
        
        # if retainCounter > 0:
        #     newListNode.next = Node(currentNode.data)
        #     newListNode = newListNode.next
        #     retainCounter -= 1
        # elif deleteCounter > 0:
        #     deleteCounter -= 1
        # else:
        #     retainCounter = i
        #     deleteCounter = j
        currentNode = currentNode.next
        counter += 1
        print("Retain Counter: {}; Delete Counter: {}; Current Node: {}".format(retainCounter, deleteCounter, currentNode.data))
        print("New Linked List:")
        print_linked_list(newHead)
        if counter == 5:
            break
        
        

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
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]
        
    temp = skip_i_delete_j(head, i, j)
    print_linked_list(temp)
    index = 0
    try:
        while temp is not None:
            if temp.data != solution[index]:
                print("Fail")
                return
            index += 1
            temp = temp.next
        print("Pass")
    except Exception as e:
        print("Fail")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
head = create_linked_list(arr)
solution = [1, 2, 5, 6, 9, 10]
test_case = [head, i, j, solution]
test_function(test_case)
# print_linked_list(test_case)

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# i = 2
# j = 3
# head = create_linked_list(arr)
# solution = [1, 2, 6, 7, 11, 12]
# test_case = [head, i, j, solution]
# test_function(test_case)
# # print_linked_list(test_case)

# arr = [1, 2, 3, 4, 5]
# i = 2
# j = 4
# head = create_linked_list(arr)
# solution = [1, 2]
# test_case = [head, i, j, solution]
# test_function(test_case)
# print_linked_list(test_case)