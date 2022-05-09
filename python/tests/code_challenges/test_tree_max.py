import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected

def test_max_val_left():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(35)
    tree.root.left.left = Node(50)

    actual = tree.find_maximum_value()
    expected = 50

    assert actual == expected

# @pytest.mark.skip("TODO")
def test_max_val_right():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(35)
    tree.root.right.left = Node(50)

    actual = tree.find_maximum_value()
    expected = 50

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_max_val_full_tree_right():
    tree = BinaryTree()
    tree.root = Node(6)
    tree.root.left = Node(10)
    tree.root.left.left = Node(20)
    tree.root.left.right = Node(30)
    tree.root.right = Node(15)
    tree.root.right.right = Node(21)
    tree.root.right.left = Node(35)

    actual = tree.find_maximum_value()
    expected = 35

    assert actual == expected

def test_max_val_full_tree_left():
    tree = BinaryTree()
    tree.root = Node(6)
    tree.root.left = Node(15)
    tree.root.left.left = Node(21)
    tree.root.left.right = Node(35)
    tree.root.right = Node(10)
    tree.root.right.right = Node(21)
    tree.root.right.left = Node(30)

    actual = tree.find_maximum_value()
    expected = 35

    assert actual == expected

def test_max_val_again():
    tree = BinaryTree()
    tree.root = Node(6)
    tree.root.left = Node(10)
    tree.root.left.left = Node(30)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected

def test_max_fail():
    tree = BinaryTree()
    actual = tree.root

    actual = tree.find_maximum_value()
    expected = 'We Aint found Root!'

    assert actual == expected
