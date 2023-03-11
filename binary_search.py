"""
worst case time complexity = O(log n) => Time reduces by half every iteration
worst case space complexity = O(n) => Space allocated only once
"""

def binary_search(list, target):
    first = 0; 
    last = len(list) - 1
    
    while first <= last:
        midpoint = (first + last)//2

        if target == list[midpoint]:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


numbers = [1, 2, 3, 4, 5, 6]

def verify(index):
    if index != None:
        print("Target found in list at position : ", index)
    else:
        print("Target not found in list")


result = binary_search(numbers, 5)
verify(result)

result = binary_search(numbers, 10)
verify(result)

result = binary_search(numbers, 1)
verify(result)
