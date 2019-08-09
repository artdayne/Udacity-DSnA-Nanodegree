def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallestPos = None
    
    for item in in_list:
        if item > 0:
            if smallestPos == None or smallestPos > item:
                smallestPos = item
    
    return smallestPos


# Test cases
print(smallest_positive([4, -6, 7, 2, -4, 10]))
print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
print(smallest_positive([88.22, -17.41, -26.53, 18.04, -44.81, 7.52, 0.0, 20.98, 11.76]))
print(smallest_positive([-98.35]))
