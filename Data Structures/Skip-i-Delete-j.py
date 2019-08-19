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
    newHead = head
    currentNode = head
    prevNode = head

    while currentNode.next:
        for iCounter in range(i, 0, -1):
            # print("Inside iCounter, step #{}".format(iCounter))
            if currentNode.next == None:
                print("Inside iCounter break")
                return newHead
            prevNode = currentNode
            currentNode = currentNode.next
        # if currentNode.next == None:
        #     return newHead
        # else:
        #     currentNode = prevNode
        print("After iCounter | Previous Node: {}; Current Node: {}".format(prevNode.data, currentNode.data))

        for jCounter in range(j, 0, -1):
            # print("Inside jCounter, step #{}".format(jCounter))
            currentNode = prevNode
            if currentNode.next.next == None:
                currentNode.next = None
                print("Inside jCounter break")
                return newHead
            currentNode.next = currentNode.next.next
        currentNode = currentNode.next
        print("After jCounter | Previous Node: {}; Current Node: {}".format(prevNode.data, currentNode.data))
        # break
    
    print("Outside the While Loop")
    return newHead

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
    print("New Linked List:")
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

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# # arr = [1, 2, 3, 4, 5, 6, 7]
# i = 2
# j = 2
# head = create_linked_list(arr)
# print_linked_list(skip_i_delete_j(head, i, j))
# solution = [1, 2, 5, 6, 9, 10]
# test_case = [head, i, j, solution]
# test_function(test_case)
# print_linked_list(test_case)

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# i = 2
# j = 3
# head = create_linked_list(arr)
# print_linked_list(skip_i_delete_j(head, i, j))
# solution = [1, 2, 6, 7, 11, 12]
# test_case = [head, i, j, solution]
# test_function(test_case)
# # print_linked_list(test_case)

arr = [1, 2, 3, 4, 5]
i = 2
j = 4
head = create_linked_list(arr)
print_linked_list(skip_i_delete_j(head, i, j))
# solution = [1, 2]
# test_case = [head, i, j, solution]
# test_function(test_case)
# print_linked_list(test_case)