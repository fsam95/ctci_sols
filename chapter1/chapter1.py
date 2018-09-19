from sets import Set
import numpy as np

# Time complexity is O(n) in the worst case assuming a good hash function for the set 
# Space complexity is O(n)
def all_unique(string):
    """
    Args: 
        string: string to test for uniqueness of characters

    Returns:
        True if string has all unique characters otherwise false
    """
    chars = Set([])
    for char in string:
        if char in chars:
            return False
        else:
            chars.add(char)
    return True

# Time complexity: O(n)
# Space complexity: O(1)
def all_unique_no_strucs(string):
    """
    Checks if a string has all unique characters with no data structures
    Args: 
        string: string to test for uniqueness of characters

    Returns:
        True if string has all unique characters otherwise false
    """
    checker = 0
    for char in string:
        bitIndexForChar = ord(char) - ord("a") 
        if checker & (1 << bitIndexForChar) > 0:
            return False
        else:
            checker = checker | (1 << bitIndexForChar)
    return True


def rotate_ninety_deg(matrix):
    """
    Rotates a numpy matrix by 90 degrees.
    Args:
        matrix: N x N matrix to rotate

    Returns: 
        rotated matrix
    """
    swaps = {}
    N = len(matrix)


        

if __name__ == "__main__":
    print(all_unique("abcd"))
    print(all_unique("abcdc"))

    print(all_unique_no_strucs("abcd"))
    print(all_unique_no_strucs("abcdc"))



