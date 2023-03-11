"""
worst case time complexity = O(n)
worst case space complexity = O(n)
"""

def linear_search(list, target):
    """
    Return position of the item if true else returns None
    """

    for i in range(len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index != None:
        print("Target found in list at position : ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6]

result = linear_search(numbers, 5)
verify(result)

result = linear_search(numbers, 10)
verify(result)

result = linear_search(numbers, 1)
verify(result)
