from data_structures.linked_list import LinkedList

def zip_lists(a,b=None):
    result = LinkedList()

    """
    Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped lis
    """
    current_a = a.head
    current_b = b.head

    if current_a == None:
        return b
    elif current_b == None:
        return a

    while current_a and current_b:
        result.append(current_a.value)
        current_a = current_a.next
        result.append(current_b.value)
        current_b = current_b.next
    while current_b:
        result.append(current_b.value)
        current_b = current_b.next
    while current_a:
        result.append(current_a.value)
        current_a = current_a.next


    return result

