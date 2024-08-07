import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root):
    if root is None:
        return float('-inf')

    st = root.value
    leftis = solution(root.left)
    rightis = solution(root.right)

    if leftis > st:
        st = leftis

    if rightis > st:
        st = rightis
    return st

def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()
