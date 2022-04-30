def binary_search(start, end, int_list, target):
    # Condition to check if element is not present
    if start <= end:
        mid = (start+end) // 2

        # Check if mid element is the target element
        if int_list[mid] == target:
            return mid

        # If not, check if lesser than mid element
        # Change range to start to mid-1, since less than mid
        elif target < int_list[mid]:
            return binary_search(start, mid-1, int_list, target)

        # Check if lesser than mid element
        # Change range to mid+1 to end, since greater than mid
        elif target > int_list[mid]:
            return binary_search(mid+1, end, int_list, target)
    else:
        return -1

binary_search(0,5,[4, 8, 15, 16, 23, 42], 15)

binary_search(0,5,[4, 8, 15, 16, 23, 42], 15)
