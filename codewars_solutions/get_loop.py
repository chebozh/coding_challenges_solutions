"""
You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

Your objective is to determine the length of the loop.

Note: do NOT mutate the nodes!

Available at: https://www.codewars.com/kata/52a89c2ea8ddc5547a000863
"""


class Node:
    def __init__(self, next=None):
        self.next = next


def loop_size(node):
    visited = []
    current_one = node
    next_one = current_one.next
    while node.next:
        if next_one not in visited:
            visited.append(next_one)
            current_one = next_one
            next_one = current_one.next
        else:
            start_of_cycle = visited.index(next_one)
            cycle_list = visited[start_of_cycle:]
            cycle_list_len = len(cycle_list)
            return cycle_list_len


# example
if __name__ == '__main__':
    nodes = [Node() for _ in range(2500)]
    for node, next_node in zip(nodes, nodes[1:]):
        node.next = next_node
    nodes[1500].next = nodes[4]
    print(loop_size(nodes[0]))
