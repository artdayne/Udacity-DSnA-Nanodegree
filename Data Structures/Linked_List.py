class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_linked_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next

def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    if len(input_list) == 0:
        return None
    elif len(input_list) == 1:
        head = Node(input_list[0])
        return head
    else:
        temp_node = Node(input_list[0])
        head = temp_node
        for i in range(len(input_list)-1):
            temp_node.next = Node(input_list[i+1])
            temp_node = temp_node.next
        return head


### Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + e)
        
        

input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list(input_list)
test_function(input_list, head)

# current_node = Node(0)
# head = current_node

# print_linked_list(current_node)

# head = Node(2)
# head.next = Node(1)
# head.next.next = Node(4)
# head.next.next.next = Node(3)
# head.next.next.next.next = Node(5)

# print_linked_list(head)