# Code

def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    
    # TODO: Write your solution here
    if len(str1.replace(" ", "")) != len(str2.replace(" ", "")):
        return False
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    for character in str1:
        str2 = str2.replace(character.lower(),"",1)
        # print(str2)
    
    if len(str2.replace(" ", "")) > 0:
        return False
    else:
        return True

# Test Cases

print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")