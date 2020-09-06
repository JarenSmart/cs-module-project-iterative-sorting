def linear_search(arr, target):
    # Loop through the array
    for i in range(0, len(arr)):
        # compare values
        if arr[i] == target:
            return i
    return -1  # not found

# Write an iterative implementation of Binary Search


def binary_search(arr, target):

    # Your code here
    if len(arr) == 0:
        return -1  # not found

    low = 0
    high = len(arr) - 1

    while low <= high:
        # hit middle
        middle = low + (high - low) // 2
        # if middle is less than target, remove right side
        if target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
        else:
            return middle
    return -1
