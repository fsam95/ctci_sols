import doctest
"""
Bit manipulation arithmetic

1. 
1010 - 0001 = 1001

2. 
1010 + 0110 = 10000

3. 
1100^1010 = 0110

4. 
1010 << 1 = 10100

5. 
1001^1001 = 0000

6. 
1001 & 1100 = 1000

7.
1010 >> 1 = 0101

8. 
0xAB + 0x11 = 0xBC
"""

def replace_n_by_m(N, M, i, j):
    """
    # step 1: clear all bits between i and j
    - do this by AND with all 1s except for bits between i and j (how do i do that?)
    # step 2: OR with M

    >>> n = 1024
    >>> m = 21
    >>> i = 2
    >>> j = 6
    >>> replace_n_by_m(n, m, i, j)
    1108
    """
    max_int = ~0

    left = max_int - ((1 << (j + 1)) - 1)
    right = ((1 << i) - 1)
    mask = left | right
    return (N & mask) | (M << i)

def largest_pow_of_two_before(num):
    """
    Arguments:
        num (int): integer greater than one

    Returns: 
        largest exponent of two that is smaller than @num

    >>> largest_pow_of_two_before(1)
    0
    >>> largest_pow_of_two_before(3)
    1
    >>> largest_pow_of_two_before(4)
    2
    """
    curr = 1
    exp = 0
    prev = 0
    while curr <= num:
        prev = exp
        exp += 1
        curr = 2 ** exp
    return prev 

def convert_whole(decimal):
    """ 
    Arguments:
        decimal (int):  decimal integer

    Returns:
        (string): Binary representation of decimal

    >>> convert_whole(2)
    '10'
    >>> convert_whole(0)
    '0'
    """
    if decimal == 0:
        return "0"
    binary_representation = ""
    largest_power = largest_pow_of_two_before(decimal)
    value = 0
    for i in range(largest_power, -1, -1):
        if value + 2 ** i <= decimal:
            binary_representation += "1"
            value += 2 ** i
        else:
            binary_representation += "0"
    return binary_representation

def binary_representation(decimal):
    """
    Arguments:
        decimal (string): decimal number (in string format) to convert to binary

    Returns:
        Binary representation of @decimal

    >>> binary_representation("3.25")
    '11.01'
    >>> binary_representation("0.25")
    '0.01'

    """
    before_fraction = int(decimal[0: decimal.index('.')])

    after_fraction = float(decimal[decimal.index('.') : ])

    binary_representation = ""
    shifted = 2 * after_fraction
    while shifted != 0: 
        if len(binary_representation) > 32:
            return "ERROR"
        if shifted >= 1:
            binary_representation += "1"
            shifted -= 1
        else:
            binary_representation += "0"
        shifted = 2 * shifted
    return convert_whole(before_fraction) + "." + binary_representation 

if __name__ == "__main__":
    doctest.testmod()
