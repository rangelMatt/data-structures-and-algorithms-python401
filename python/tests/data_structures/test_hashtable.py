from ctypes import sizeof
import pytest
from data_structures.hashtable import Hashtable

# set
# Arguments: key, value
# Returns: nothing
# This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
# Should a given key already exist, replace its value from the value argument given to this method.
# get
# Arguments: key
# Returns: Value associated with that key in the table
# contains
# Arguments: key
# Returns: Boolean, indicating if the key exists in the table already.
# keys
# Returns: Collection of keys
# hash
# Arguments: key
# Returns: Index in the collection for that key

def test_exists():
    assert Hashtable

def test_set_exists():
    assert Hashtable.set

def test_get_exists():
    assert Hashtable.get

def test_hash_exists():
    assert Hashtable.hash

def test_contains_exists():
    assert Hashtable.contains

def test_keys_exists():
    assert Hashtable.keys

# tests creating a new Hashtable
def test_create():
    ht = Hashtable()
    actual = ht.size
    expected = 1024
    assert actual == expected

# @pytest.mark.skip("TODO")
# def test_get_nonexistent():
#     ht = Hashtable()
#     ht.set("apple", "Used for apple sauce")
#     actual = ht.get("banana")
#     expected = None
#     assert actual == expected

def test_hash():
    """
    hash
    Arguments: key
    Returns: Index in the collection for that key
    """
    # make a hashtable
    ht = Hashtable()

    index = ht.hash("cat")
    # assert that index is within range
    assert 0 <= index < ht.size

def test_set_apple():
    ht = Hashtable()
    ht.set("fruit","apple")
    fruit_index = ht.hash("fruit")
    actual = ht._buckets[fruit_index]
    expected = ("fruit","apple")
    assert actual.head.value == expected

def test_get_apple():
    ht = Hashtable()
    ht.set("fruit","apple")

    actual = ht.get("fruit")
    expected = ("apple")
    assert actual == expected

def test_collisions():
    ht = Hashtable()
    ht.set("cat","Josie")
    ht.set("act","A Contemporary Theater")
    ht.set("tac","Taco Tuesday")

    assert ht.get("cat") == "Josie"
    assert ht.get("act") == "A Contemporary Theater"
    assert ht.get("tac") == "Taco Tuesday"
    actual = ht.keys()
    expected = {"cat","act","tac"}
    assert actual == expected

def test_contains_true():
    ht = Hashtable()
    ht.set('cat', 'josie')
    expected = True
    actual = ht.contains('cat')
    assert actual == expected


def test_contains_false():
    ht = Hashtable()
    ht.set('cat', 'josie')
    expected = False
    actual = ht.contains('act')
    assert actual == expected

def test_keys_in_hashtable():
    ht = Hashtable()
    ht.set('cat', 'josie')
    ht.set('act', 'a contemporary theatre')
    ht.set('tac', 'taco tuesday')
    actual = ht.keys()
    expected = {'cat', 'act', 'tac'}
    assert actual == expected


def test_keys_not_in_hashtable():
    ht = Hashtable()
    ht.set('cat', 'josie')
    ht.set('act', 'a contemporary theatre')
    ht.set('guc', 'taco tuesday')
    actual = ht.keys()
    expected = ['cat', 'act', 'tac']
    assert actual != expected

# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected


#Hot to handle updates
@pytest.mark.skip("TODO")
def test_set_update():
    ht = Hashtable()
    ht.set("cat","josie")
    ht.set("cat", "taco tuesday")

    actual = ht.get("cat")
    expected = "taco tuesday"
    assert actual == expected
