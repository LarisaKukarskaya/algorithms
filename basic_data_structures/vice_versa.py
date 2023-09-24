def solution(node):
    a = node
    b = a.next
    a.next = None
    a.prev = b
    while b is not None:
        b.prev = b.next
        b.next = a
        a = b
        b = b.prev
    node = a
    return node
