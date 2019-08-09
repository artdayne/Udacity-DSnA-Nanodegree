class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        if self.head is None:
            # print("in pre-pend self.head is none")
            self.head = Node(value)
            return
        
        # Move to the head (the first node)
        newHeadNode = Node(value)
        # print("newHeadNode value in pre-pend is: {} and its next is {}".format(newHeadNode.value, newHeadNode.next))
        newHeadNode.next = self.head
        self.head = newHeadNode
        # print("Self.head value in pre-pend is: {} and the Value is {}".format(self.head.value, value))
        # print("newHeadNode value in pre-pend is: {} and its next is {}".format(newHeadNode.value, newHeadNode.next))

    def append(self, value):
        if self.head is None:
            # print("in append self.head is none")
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        # print("Node value before loop in append: {}".format(node.value))

        counter = 0
        while node.next:
            counter += 1
            node = node.next
        # print("Counter value in append: {}".format(counter))

        node.next = Node(value)
        # print("Value assigned to latest appended node: {}".format(node.next.value))
        return

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return None
        
        node = self.head
        
        while node:
            if node.value == value:
                return node
            node = node.next
        
        return node
    
    def remove(self, value):
        """ Remove first occurrence of value. """
        
        # TODO: Write function to remove here
        
        pass
    
    def pop(self):
        """ Return the first node's value and remove it from the list. """
        
        # TODO: Write function to pop here
        
        pass
    
    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        
        # TODO: Write function to insert here
        
        pass
    
    def size(self):
        """ Return the size or length of the linked list. """
        
        
        # TODO: Write function to get size here

    def to_list(self):
        if self.head is None:
            return None
        
        python_list = []
        
        node = self.head
        while node.next:
            python_list.append(node.value)
            node = node.next
        python_list.append(node.value)

        return python_list

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

## Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
    
# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# # Test remove
# linked_list.remove(1)
# assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
# linked_list.remove(3)
# assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
# linked_list.remove(3)
# assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# # Test pop
# value = linked_list.pop()
# assert value == 2, f"list contents: {linked_list.to_list()}"
# assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# # Test insert 
# linked_list.insert(5, 0)
# assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
# linked_list.insert(2, 1)
# assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
# linked_list.insert(3, 6)
# assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# # Test size
# assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"        

# input_list = [1, 2, 3, 4, 5, 6]
# head = create_linked_list(input_list)
# test_function(input_list, head)

# input_list = [1]
# head = create_linked_list(input_list)
# test_function(input_list, head)

# input_list = []
# head = create_linked_list(input_list)
# test_function(input_list, head)