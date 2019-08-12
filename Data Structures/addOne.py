def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    counter = 0
    arrLen = len(arr)
    while counter < arrLen:
        if arr[arrLen-counter-1] < 9:
            arr[arrLen-counter-1] += 1
            return arr
        else:
            arr[arrLen-counter-1] = 0
            if arrLen - counter - 1 == 0:
                arr.insert(0,1)
                return arr
        counter += 1
    ########## ALTERNATE SOLUTION ##########
    # output = 1

    # for i in range(len(arr), 0, -1):
    #     output = output + arr[i - 1]
    #     borrow = output//10
    #     if borrow == 0:
    #         arr[i - 1] = output
    #         break
    #     else:
    #         arr[i - 1] = output % 10
    #         output = borrow
    # arr = [borrow] + arr
    # index = 0
    # while arr[index]==0:
    #     index += 1
    # return arr[index:]
    ########## END OF ALT SOLUTION ##########

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")      

arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 9]
solution = [1, 3, 0]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)