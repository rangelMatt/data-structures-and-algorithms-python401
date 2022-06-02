from data_structures.hashtable import Hashtable



'''
left join = grab all from left and intersection of left and right.
'''


def left_join(left_table, right_table):
    # create an empty list
    to_the_left = []

    # grab key from left hash/table
    for key in left_table:

        # for each item in left assign join_left variable with key, value in left and value in right table(if the same key exist in the left). get() returns the value of the item with provided key
        # append the outcome to empty list
        join_left = [key, left_table.get(key), right_table.get(key)or "NONE"]
        to_the_left.append(join_left)

    # return output
    return to_the_left
