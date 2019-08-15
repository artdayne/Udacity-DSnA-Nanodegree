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
    tail = newHead
    currentNode = head

    while currentNode.next:
        count = 0
        for count in range(i):
            if currentNode.next is not None:
                currentNode = currentNode.next
            else:
                break
            tail.next = Node(currentNode.data)
            tail = tail.next
            count += 1
        count = 0
        for count in range(j):
            if currentNode.next is not None:
                currentNode = currentNode.next
            else:
                break
            count += 1
    
    return newHead
    # currentNode = head
    # retainHead = head
    # retain = i
    # delete = j

    # while currentNode.next:
        
        # if retain > 0:
        #     currentNode = currentNode.next
        #     retain -= 1
        #     # print_linked_list(retainHead)
        # elif delete > 0:
        #     currentNode.next = currentNode.next.next
        #     delete -= 1
        #     # print_linked_list(retainHead)
        # else:
        #     retain = i
        #     delete = j
    # return retainHead

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

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 3
head = create_linked_list(arr)
solution = [1, 2, 6, 7, 11, 12]
test_case = [head, i, j, solution]
test_function(test_case)
# print_linked_list(test_case)

arr = [1, 2, 3, 4, 5]
i = 2
j = 4
head = create_linked_list(arr)
solution = [1, 2]
test_case = [head, i, j, solution]
test_function(test_case)
# print_linked_list(test_case)