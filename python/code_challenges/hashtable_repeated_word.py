# from data_structures.hashtable import Hashtable
# from collections import Counter
import re

def first_repeated_word(word):
    if word is None:
        return None

    # first regex argument is searching for characters specified to that string
    # second regex argument is replacing those characters with that argument
    # third regex argument is taking in the string
    regex= re.compile('[^a-zA-Z ]')
    new_string = regex.sub('', word)
    # Splits the given string into words separated by space and turn the words into lower case
    words = new_string.lower().split()

    # The set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements, commonly called Set
    dictionary = set()

    # Iterate through the set of words
    for value in words:

        # check if the value is in the dictionary
        if value in dictionary:

            # return the value
            return value

            # else add the value to the dictionary
        else:
            # The set add() method adds a given element to a set if the element is not present in the set.
            dictionary.add(value)




    # words = word.split(" ")

    # dictionary = {}

    # for word in words:
    #     if dictionary[word] is not None:
    #         return word
    #     else:
    #         return None
    #         # dictionary[word] = word
