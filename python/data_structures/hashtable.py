from data_structures.linked_list import LinkedList

# creates Hashtable
class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024, key=None):
        self.size = size
        # array of none, multiplied by size, this will represent empty units till we put stuff in it

        # pre generated list of objects
        self._buckets = [None] * self.size

        self.key = key


    # hash method that takes in a key
    def hash(self,key):

        # Add or multiply all the ASCII values together.
        sum_of_chars = 0

        for char in key:
            sum_of_chars += ord(char)

        # Multiply it by a prime number such as 599.
        primed = sum_of_chars * 599


        # Use modulo to get the remainder of the result, when divided by the total size of the array.
        index = primed % self.size

        # Insert into the array at that index.
        return index

    #
    def set(self, key, value):
        index = self.hash(key)

        bucket = self._buckets[index]
        # print(bucket)

        if bucket is None:
            # then make make bucket to a linked list
            bucket = LinkedList()

            # bucket in self._buckets at index
            self._buckets[index] = bucket

        #TODO: handle updates vs adds
        bucket.append((key, value))

    def get(self, key):
        # get to the hash of the key
        #convert the key into an index, the hash function does it
        index = self.hash(key)
        # go the the address in _buckets and grab the bucket
        bucket = self._buckets[index]

        current = bucket.head

        while current:
            pair = current.value    #0       1
            current_key = pair[0] #("cat","josie")
            if current_key == key:
                # value associated with the key
                return pair[1]

            current = current.next
        return None

    def contains(self, key):
        if self.get(key):
            return True
        else:
            return False

    def keys(self):
        all_the_keys = set()

        for bucket in self._buckets:
            if bucket is not None:
                current = bucket.head
                while current:
                    pair = current.value
                    current_key = pair[0]
                    all_the_keys.add(current_key)
                    current = current.next
        return all_the_keys
