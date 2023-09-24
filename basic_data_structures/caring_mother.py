def solution(node, elem):
    count = 0
    while elem != count:
        if node == None:
            return - 1
        if elem == node.value:
            return count
        else:
            node = node.next_item
            count += 1
