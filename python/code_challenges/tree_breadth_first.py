
from data_structures.queue import Queue


def breadth_first(tree):
    result = []

    if tree is None:
        return result
    if tree.root is None:
        return result

    b_que = Queue()
    b_que.enqueue(tree.root)

    while not b_que.is_empty():
        front_node = b_que.dequeue()
        result.append(front_node.value)

        if front_node.left is not None:
            b_que.enqueue(front_node.left)

        if  front_node.right is not None:
            b_que.enqueue(front_node.right)

    return result


