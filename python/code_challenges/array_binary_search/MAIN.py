# binary = [1, 2, 3, 5, 6, 7]

def search_array(start, end, int_list, target):

    if start <= end:
        mid = (start+end) // 2
        # base case/ stopping condition
        if int_list[mid] == target:
            return mid

        elif target < int_list[mid]:
            return search_array(start, mid-1, int_list, target)

        elif target > int_list[mid]:
            return search_array(mid+1, end, int_list, target)
    else:
        return -1


print(search_array(0, 5, [1, 2, 3, 5, 6, 7], 4))
print(search_array(0, 5, [4, 8, 15, 16, 23, 42], 15))
