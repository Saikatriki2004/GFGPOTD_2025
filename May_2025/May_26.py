class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)
        # Empty list case
        if head is None:
            new_node.next = new_node
            return new_node
        curr = head
        # Find insertion point
        while True:
            # Case 1: between two nodes in sorted order
            if curr.data <= data <= curr.next.data:
                break
            # Case 2: at the boundary between max and min
            if curr.data > curr.next.data:
                if data >= curr.data or data <= curr.next.data:
                    break
            curr = curr.next
            # If full loop completed
            if curr == head:
                break
        # Insert new_node
        new_node.next = curr.next
        curr.next = new_node
        # Determine new head
        # If inserting before the current head, new_node becomes new head
        if data < head.data:
            return new_node
        return head
