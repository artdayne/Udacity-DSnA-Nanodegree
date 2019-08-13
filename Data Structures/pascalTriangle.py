# Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.
# For exmaple, if n = 4, then output = [1, 4, 6, 4, 1].
# To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html

import math

def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    nth_row = list()

    for num in range(n+1):
        nth_row.append(math.factorial(n) / (math.factorial(num) * math.factorial(n - num)))
    
    print(nth_row)
    return nth_row

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")

# n = 0
# solution = [1]

# test_case = [n, solution]
# test_function(test_case)

# n = 1
# solution = [1, 1]

# test_case = [n, solution]
# test_function(test_case)

# n = 2
# solution = [1, 2, 1]

# test_case = [n, solution]
# test_function(test_case)

# n = 3
# solution = [1, 3, 3, 1]

# test_case = [n, solution]
# test_function(test_case)

# n = 4
# solution = [1, 4, 6, 4, 1]

# test_case = [n, solution]
# test_function(test_case)

nth_row_pascal(11)