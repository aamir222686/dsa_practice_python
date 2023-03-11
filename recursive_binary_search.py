"""
worst case time complexity = O(log n) => Time reduces by half every iteration
worst case space complexity = O(log n) => n, n/2, n/4 ... new lists created every pass
"""

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)
            

numbers = [1, 2, 3, 4, 5, 6]

def verify(result):
    if result == True:
        print("Target found in list ", result) 
    else:
        print("Target not found in list ", False)


result = recursive_binary_search(numbers, 5)
verify(result)

result = recursive_binary_search(numbers, 10)
verify(result)

result = recursive_binary_search(numbers, 1)
verify(result)


